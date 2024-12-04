# Results vs. 3.13.0

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: ba20c7c
- commit date: 2024-12-04
- overall geometric mean: 1.037x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 257 ms: 1.04x faster                                                       |
| docutils       | 2.59 sec                                               | 2.59 sec: 1.00x faster                                                     |
| html5lib       | 64.2 ms                                                | 64.6 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io              | 842 ms                                                 | 608 ms: 1.39x faster                                                       |
| async_tree_io_tg           | 857 ms                                                 | 625 ms: 1.37x faster                                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 344 ms: 1.35x faster                                                       |
| async_tree_none            | 351 ms                                                 | 275 ms: 1.27x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 350 ms: 1.26x faster                                                       |
| async_tree_none_tg         | 321 ms                                                 | 276 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 501 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 493 ms: 1.11x faster                                                       |
| async_generators           | 436 ms                                                 | 426 ms: 1.02x faster                                                       |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 80.7 ms: 1.02x slower                                                      |
| pidigits       | 186 ms                                                 | 191 ms: 1.02x slower                                                       |
| nbody          | 87.0 ms                                                | 93.6 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.45 ms: 1.08x faster                                                      |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                       |
| regex_v8       | 26.2 ms                                                | 26.1 ms: 1.00x faster                                                      |
| regex_dna      | 218 ms                                                 | 220 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                       |
| json_loads           | 27.2 us                                                | 26.9 us: 1.01x faster                                                      |
| tomli_loads          | 2.14 sec                                               | 2.13 sec: 1.01x faster                                                     |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.01x slower                                                       |
| xml_etree_process    | 60.6 ms                                                | 61.6 ms: 1.02x slower                                                      |
| xml_etree_generate   | 86.7 ms                                                | 88.3 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.03x slower                                                       |
| pickle_pure_python   | 310 us                                                 | 324 us: 1.04x slower                                                       |
| json_dumps           | 10.6 ms                                                | 11.5 ms: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                      |
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 32.2 ms: 1.09x faster                                                      |
| genshi_text     | 23.5 ms                                                | 22.2 ms: 1.06x faster                                                      |
| genshi_xml      | 50.9 ms                                                | 50.3 ms: 1.01x faster                                                      |
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io              | 842 ms                                                 | 608 ms: 1.39x faster                                                       |
| async_tree_io_tg           | 857 ms                                                 | 625 ms: 1.37x faster                                                       |
| deepcopy                   | 358 us                                                 | 262 us: 1.37x faster                                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 344 ms: 1.35x faster                                                       |
| async_tree_none            | 351 ms                                                 | 275 ms: 1.27x faster                                                       |
| deepcopy_memo              | 39.1 us                                                | 30.7 us: 1.27x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 350 ms: 1.26x faster                                                       |
| go                         | 144 ms                                                 | 121 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.20 us                                                | 2.70 us: 1.18x faster                                                      |
| async_tree_none_tg         | 321 ms                                                 | 276 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 501 ms: 1.15x faster                                                       |
| pylint                     | 313 ms                                                 | 272 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 493 ms: 1.11x faster                                                       |
| json                       | 5.36 ms                                                | 4.89 ms: 1.10x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.10 sec: 1.09x faster                                                     |
| django_template            | 35.2 ms                                                | 32.2 ms: 1.09x faster                                                      |
| regex_effbot               | 3.73 ms                                                | 3.45 ms: 1.08x faster                                                      |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                      |
| telco                      | 8.54 ms                                                | 7.92 ms: 1.08x faster                                                      |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                       |
| k_core                     | 2.35 sec                                               | 2.21 sec: 1.07x faster                                                     |
| thrift                     | 809 us                                                 | 762 us: 1.06x faster                                                       |
| create_gc_cycles           | 2.41 ms                                                | 2.27 ms: 1.06x faster                                                      |
| genshi_text                | 23.5 ms                                                | 22.2 ms: 1.06x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.05x faster                                                       |
| mdp                        | 2.72 sec                                               | 2.60 sec: 1.05x faster                                                     |
| crypto_pyaes               | 75.3 ms                                                | 72.1 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.83 ms: 1.04x faster                                                      |
| 2to3                       | 267 ms                                                 | 257 ms: 1.04x faster                                                       |
| richards                   | 48.7 ms                                                | 46.8 ms: 1.04x faster                                                      |
| logging_format             | 6.40 us                                                | 6.17 us: 1.04x faster                                                      |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                       |
| sqlalchemy_imperative      | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                      |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.03x faster                                                       |
| richards_super             | 54.9 ms                                                | 53.3 ms: 1.03x faster                                                      |
| bpe_tokeniser              | 4.75 sec                                               | 4.61 sec: 1.03x faster                                                     |
| async_generators           | 436 ms                                                 | 426 ms: 1.02x faster                                                       |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                       |
| logging_simple             | 5.72 us                                                | 5.60 us: 1.02x faster                                                      |
| sympy_str                  | 275 ms                                                 | 270 ms: 1.02x faster                                                       |
| sympy_expand               | 463 ms                                                 | 456 ms: 1.02x faster                                                       |
| json_loads                 | 27.2 us                                                | 26.9 us: 1.01x faster                                                      |
| connected_components       | 444 ms                                                 | 438 ms: 1.01x faster                                                       |
| genshi_xml                 | 50.9 ms                                                | 50.3 ms: 1.01x faster                                                      |
| typing_runtime_protocols   | 165 us                                                 | 163 us: 1.01x faster                                                       |
| pprint_pformat             | 1.49 sec                                               | 1.49 sec: 1.01x faster                                                     |
| tomli_loads                | 2.14 sec                                               | 2.13 sec: 1.01x faster                                                     |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                      |
| regex_v8                   | 26.2 ms                                                | 26.1 ms: 1.00x faster                                                      |
| docutils                   | 2.59 sec                                               | 2.59 sec: 1.00x faster                                                     |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.00x slower                                                       |
| regex_dna                  | 218 ms                                                 | 220 ms: 1.00x slower                                                       |
| sqlglot_optimize           | 53.7 ms                                                | 54.1 ms: 1.01x slower                                                      |
| html5lib                   | 64.2 ms                                                | 64.6 ms: 1.01x slower                                                      |
| scimark_fft                | 364 ms                                                 | 367 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.01x slower                                                       |
| dulwich_log                | 64.3 ms                                                | 64.9 ms: 1.01x slower                                                      |
| pyflate                    | 471 ms                                                 | 475 ms: 1.01x slower                                                       |
| python_startup_no_site     | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                      |
| xml_etree_process          | 60.6 ms                                                | 61.6 ms: 1.02x slower                                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 68.6 ms: 1.02x slower                                                      |
| xml_etree_generate         | 86.7 ms                                                | 88.3 ms: 1.02x slower                                                      |
| coverage                   | 84.0 ms                                                | 85.6 ms: 1.02x slower                                                      |
| float                      | 79.2 ms                                                | 80.7 ms: 1.02x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.02x slower                                                      |
| sqlglot_transpile          | 1.58 ms                                                | 1.62 ms: 1.02x slower                                                      |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                      |
| hexiom                     | 6.16 ms                                                | 6.30 ms: 1.02x slower                                                      |
| pidigits                   | 186 ms                                                 | 191 ms: 1.02x slower                                                       |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                                       |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                      |
| scimark_sor                | 124 ms                                                 | 127 ms: 1.03x slower                                                       |
| mako                       | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                      |
| raytrace                   | 267 ms                                                 | 275 ms: 1.03x slower                                                       |
| nqueens                    | 78.4 ms                                                | 80.7 ms: 1.03x slower                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 104 ms: 1.03x slower                                                       |
| deltablue                  | 3.23 ms                                                | 3.35 ms: 1.04x slower                                                      |
| bench_thread_pool          | 822 us                                                 | 854 us: 1.04x slower                                                       |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                      |
| pickle_pure_python         | 310 us                                                 | 324 us: 1.04x slower                                                       |
| logging_silent             | 102 ns                                                 | 107 ns: 1.05x slower                                                       |
| chaos                      | 58.1 ms                                                | 61.2 ms: 1.05x slower                                                      |
| nbody                      | 87.0 ms                                                | 93.6 ms: 1.08x slower                                                      |
| json_dumps                 | 10.6 ms                                                | 11.5 ms: 1.09x slower                                                      |
| gc_traversal               | 4.37 ms                                                | 4.82 ms: 1.10x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 80.6 ms: 3.36x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (7): sphinx, shortest_path, sqlglot_normalize, pprint_safe_repr, asyncio_websockets, fannkuch, generators
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241204-3.14.0a2+-ba20c7c/bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x