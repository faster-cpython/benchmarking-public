# Results vs. 3.13.0

- fork: faster-cpython
- ref: mark_first_gc
- machine: linux-x86_64
- commit hash: 278059b
- commit date: 2024-11-15
- overall geometric mean: 1.040x faster
- HPT reliability: 96.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 263 ms: 1.02x faster                                                      |
| docutils       | 2.59 sec                                               | 2.65 sec: 1.02x slower                                                    |
| html5lib       | 64.2 ms                                                | 67.5 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 857 ms                                                 | 627 ms: 1.37x faster                                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 352 ms: 1.32x faster                                                      |
| async_tree_io              | 842 ms                                                 | 643 ms: 1.31x faster                                                      |
| async_tree_none            | 351 ms                                                 | 283 ms: 1.24x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 358 ms: 1.24x faster                                                      |
| async_tree_none_tg         | 321 ms                                                 | 271 ms: 1.18x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 514 ms: 1.12x faster                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 502 ms: 1.09x faster                                                      |
| async_generators           | 436 ms                                                 | 433 ms: 1.01x faster                                                      |
| coroutines                 | 22.7 ms                                                | 23.8 ms: 1.05x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.16x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 192 ms: 1.03x slower                                                      |
| float          | 79.2 ms                                                | 84.2 ms: 1.06x slower                                                     |
| nbody          | 87.0 ms                                                | 96.5 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                     |
| regex_compile  | 132 ms                                                 | 130 ms: 1.01x faster                                                      |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                                      |
| regex_effbot   | 3.73 ms                                                | 3.86 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                                     |
| tomli_loads          | 2.14 sec                                               | 2.11 sec: 1.01x faster                                                    |
| xml_etree_generate   | 86.7 ms                                                | 87.9 ms: 1.01x slower                                                     |
| xml_etree_process    | 60.6 ms                                                | 61.9 ms: 1.02x slower                                                     |
| unpickle_pure_python | 216 us                                                 | 221 us: 1.02x slower                                                      |
| pickle_pure_python   | 310 us                                                 | 324 us: 1.04x slower                                                      |
| json_dumps           | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 117 ms: 1.15x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 6.72 ms: 1.04x faster                                                     |
| python_startup         | 12.5 ms                                                | 12.4 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 32.9 ms: 1.07x faster                                                     |
| genshi_text     | 23.5 ms                                                | 22.2 ms: 1.06x faster                                                     |
| genshi_xml      | 50.9 ms                                                | 51.4 ms: 1.01x slower                                                     |
| mako            | 11.1 ms                                                | 11.6 ms: 1.04x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| gc_traversal               | 4.37 ms                                                | 2.29 ms: 1.91x faster                                                     |
| create_gc_cycles           | 2.41 ms                                                | 1.67 ms: 1.44x faster                                                     |
| async_tree_io_tg           | 857 ms                                                 | 627 ms: 1.37x faster                                                      |
| deepcopy                   | 358 us                                                 | 262 us: 1.37x faster                                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 352 ms: 1.32x faster                                                      |
| async_tree_io              | 842 ms                                                 | 643 ms: 1.31x faster                                                      |
| deepcopy_memo              | 39.1 us                                                | 30.8 us: 1.27x faster                                                     |
| async_tree_none            | 351 ms                                                 | 283 ms: 1.24x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 358 ms: 1.24x faster                                                      |
| go                         | 144 ms                                                 | 121 ms: 1.19x faster                                                      |
| deepcopy_reduce            | 3.20 us                                                | 2.69 us: 1.19x faster                                                     |
| async_tree_none_tg         | 321 ms                                                 | 271 ms: 1.18x faster                                                      |
| pylint                     | 313 ms                                                 | 277 ms: 1.13x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 514 ms: 1.12x faster                                                      |
| telco                      | 8.54 ms                                                | 7.83 ms: 1.09x faster                                                     |
| json                       | 5.36 ms                                                | 4.92 ms: 1.09x faster                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 502 ms: 1.09x faster                                                      |
| mdp                        | 2.72 sec                                               | 2.51 sec: 1.09x faster                                                    |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.09x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                    |
| django_template            | 35.2 ms                                                | 32.9 ms: 1.07x faster                                                     |
| genshi_text                | 23.5 ms                                                | 22.2 ms: 1.06x faster                                                     |
| regex_v8                   | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                     |
| k_core                     | 2.35 sec                                               | 2.22 sec: 1.06x faster                                                    |
| thrift                     | 809 us                                                 | 776 us: 1.04x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                      |
| richards                   | 48.7 ms                                                | 46.8 ms: 1.04x faster                                                     |
| generators                 | 29.0 ms                                                | 27.9 ms: 1.04x faster                                                     |
| sqlalchemy_imperative      | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                     |
| python_startup_no_site     | 6.96 ms                                                | 6.72 ms: 1.04x faster                                                     |
| richards_super             | 54.9 ms                                                | 53.2 ms: 1.03x faster                                                     |
| logging_simple             | 5.72 us                                                | 5.57 us: 1.03x faster                                                     |
| logging_format             | 6.40 us                                                | 6.23 us: 1.03x faster                                                     |
| sympy_str                  | 275 ms                                                 | 269 ms: 1.02x faster                                                      |
| sympy_expand               | 463 ms                                                 | 454 ms: 1.02x faster                                                      |
| typing_runtime_protocols   | 165 us                                                 | 161 us: 1.02x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                      |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                                     |
| 2to3                       | 267 ms                                                 | 263 ms: 1.02x faster                                                      |
| regex_compile              | 132 ms                                                 | 130 ms: 1.01x faster                                                      |
| tomli_loads                | 2.14 sec                                               | 2.11 sec: 1.01x faster                                                    |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.98 ms: 1.01x faster                                                     |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                                      |
| crypto_pyaes               | 75.3 ms                                                | 74.6 ms: 1.01x faster                                                     |
| pprint_pformat             | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                    |
| python_startup             | 12.5 ms                                                | 12.4 ms: 1.01x faster                                                     |
| async_generators           | 436 ms                                                 | 433 ms: 1.01x faster                                                      |
| sympy_integrate            | 19.9 ms                                                | 19.9 ms: 1.00x slower                                                     |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.01x slower                                                      |
| genshi_xml                 | 50.9 ms                                                | 51.4 ms: 1.01x slower                                                     |
| regex_dna                  | 218 ms                                                 | 221 ms: 1.01x slower                                                      |
| sqlglot_optimize           | 53.7 ms                                                | 54.3 ms: 1.01x slower                                                     |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.01x slower                                                      |
| dulwich_log                | 64.3 ms                                                | 65.1 ms: 1.01x slower                                                     |
| xml_etree_generate         | 86.7 ms                                                | 87.9 ms: 1.01x slower                                                     |
| scimark_monte_carlo        | 67.4 ms                                                | 68.6 ms: 1.02x slower                                                     |
| xml_etree_process          | 60.6 ms                                                | 61.9 ms: 1.02x slower                                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.62 ms: 1.02x slower                                                     |
| unpickle_pure_python       | 216 us                                                 | 221 us: 1.02x slower                                                      |
| docutils                   | 2.59 sec                                               | 2.65 sec: 1.02x slower                                                    |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.02x slower                                                     |
| fannkuch                   | 404 ms                                                 | 415 ms: 1.03x slower                                                      |
| bpe_tokeniser              | 4.75 sec                                               | 4.87 sec: 1.03x slower                                                    |
| nqueens                    | 78.4 ms                                                | 80.8 ms: 1.03x slower                                                     |
| pidigits                   | 186 ms                                                 | 192 ms: 1.03x slower                                                      |
| scimark_sor                | 124 ms                                                 | 127 ms: 1.03x slower                                                      |
| raytrace                   | 267 ms                                                 | 276 ms: 1.03x slower                                                      |
| hexiom                     | 6.16 ms                                                | 6.37 ms: 1.03x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.03x slower                                                     |
| scimark_lu                 | 113 ms                                                 | 117 ms: 1.03x slower                                                      |
| regex_effbot               | 3.73 ms                                                | 3.86 ms: 1.03x slower                                                     |
| bench_thread_pool          | 822 us                                                 | 851 us: 1.04x slower                                                      |
| mako                       | 11.1 ms                                                | 11.6 ms: 1.04x slower                                                     |
| pickle_pure_python         | 310 us                                                 | 324 us: 1.04x slower                                                      |
| coverage                   | 84.0 ms                                                | 88.1 ms: 1.05x slower                                                     |
| coroutines                 | 22.7 ms                                                | 23.8 ms: 1.05x slower                                                     |
| html5lib                   | 64.2 ms                                                | 67.5 ms: 1.05x slower                                                     |
| json_dumps                 | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                     |
| deltablue                  | 3.23 ms                                                | 3.42 ms: 1.06x slower                                                     |
| chaos                      | 58.1 ms                                                | 61.5 ms: 1.06x slower                                                     |
| float                      | 79.2 ms                                                | 84.2 ms: 1.06x slower                                                     |
| logging_silent             | 102 ns                                                 | 109 ns: 1.07x slower                                                      |
| nbody                      | 87.0 ms                                                | 96.5 ms: 1.11x slower                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 117 ms: 1.15x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 83.5 ms: 3.48x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (8): connected_components, xml_etree_parse, shortest_path, sphinx, scimark_fft, pprint_safe_repr, pyflate, asyncio_websockets
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241115-3.14.0a1+-278059b/bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.040x faster
# HPT report

- Reliability score: 96.76% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x