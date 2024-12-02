# Results vs. 3.13.0

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: 07f228b
- commit date: 2024-12-02
- overall geometric mean: 1.032x faster
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 256 ms: 1.04x faster                                                       |
| html5lib       | 64.2 ms                                                | 63.8 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io              | 842 ms                                                 | 636 ms: 1.32x faster                                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 352 ms: 1.32x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 352 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 857 ms                                                 | 683 ms: 1.25x faster                                                       |
| async_tree_none            | 351 ms                                                 | 289 ms: 1.21x faster                                                       |
| async_tree_none_tg         | 321 ms                                                 | 286 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 522 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 514 ms: 1.06x faster                                                       |
| async_generators           | 436 ms                                                 | 424 ms: 1.03x faster                                                       |
| coroutines                 | 22.7 ms                                                | 23.8 ms: 1.05x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                       |
| nbody          | 87.0 ms                                                | 94.5 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.35 ms: 1.12x faster                                                      |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                       |
| regex_v8       | 26.2 ms                                                | 25.9 ms: 1.01x faster                                                      |
| regex_dna      | 218 ms                                                 | 222 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.06x faster                                                       |
| json_loads           | 27.2 us                                                | 26.1 us: 1.04x faster                                                      |
| tomli_loads          | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                     |
| xml_etree_process    | 60.6 ms                                                | 60.2 ms: 1.01x faster                                                      |
| unpickle_pure_python | 216 us                                                 | 220 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.03x slower                                                       |
| pickle_pure_python   | 310 us                                                 | 330 us: 1.06x slower                                                       |
| json_dumps           | 10.6 ms                                                | 11.5 ms: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                      |
| python_startup         | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 31.8 ms: 1.11x faster                                                      |
| genshi_text     | 23.5 ms                                                | 22.7 ms: 1.04x faster                                                      |
| genshi_xml      | 50.9 ms                                                | 49.6 ms: 1.03x faster                                                      |
| mako            | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 261 us: 1.37x faster                                                       |
| async_tree_io              | 842 ms                                                 | 636 ms: 1.32x faster                                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 352 ms: 1.32x faster                                                       |
| deepcopy_memo              | 39.1 us                                                | 30.8 us: 1.27x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 352 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 857 ms                                                 | 683 ms: 1.25x faster                                                       |
| go                         | 144 ms                                                 | 118 ms: 1.22x faster                                                       |
| async_tree_none            | 351 ms                                                 | 289 ms: 1.21x faster                                                       |
| deepcopy_reduce            | 3.20 us                                                | 2.69 us: 1.19x faster                                                      |
| pylint                     | 313 ms                                                 | 274 ms: 1.14x faster                                                       |
| async_tree_none_tg         | 321 ms                                                 | 286 ms: 1.12x faster                                                       |
| regex_effbot               | 3.73 ms                                                | 3.35 ms: 1.12x faster                                                      |
| json                       | 5.36 ms                                                | 4.85 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 522 ms: 1.11x faster                                                       |
| django_template            | 35.2 ms                                                | 31.8 ms: 1.11x faster                                                      |
| telco                      | 8.54 ms                                                | 7.82 ms: 1.09x faster                                                      |
| pathlib                    | 17.5 ms                                                | 16.5 ms: 1.07x faster                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 514 ms: 1.06x faster                                                       |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.75 ms: 1.06x faster                                                      |
| thrift                     | 809 us                                                 | 765 us: 1.06x faster                                                       |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.06x faster                                                       |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.05x faster                                                       |
| json_loads                 | 27.2 us                                                | 26.1 us: 1.04x faster                                                      |
| generators                 | 29.0 ms                                                | 27.8 ms: 1.04x faster                                                      |
| 2to3                       | 267 ms                                                 | 256 ms: 1.04x faster                                                       |
| richards                   | 48.7 ms                                                | 46.8 ms: 1.04x faster                                                      |
| pyflate                    | 471 ms                                                 | 453 ms: 1.04x faster                                                       |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                     |
| genshi_text                | 23.5 ms                                                | 22.7 ms: 1.04x faster                                                      |
| logging_format             | 6.40 us                                                | 6.17 us: 1.04x faster                                                      |
| crypto_pyaes               | 75.3 ms                                                | 72.9 ms: 1.03x faster                                                      |
| richards_super             | 54.9 ms                                                | 53.1 ms: 1.03x faster                                                      |
| sqlalchemy_imperative      | 17.1 ms                                                | 16.5 ms: 1.03x faster                                                      |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                       |
| async_generators           | 436 ms                                                 | 424 ms: 1.03x faster                                                       |
| tomli_loads                | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                     |
| genshi_xml                 | 50.9 ms                                                | 49.6 ms: 1.03x faster                                                      |
| bpe_tokeniser              | 4.75 sec                                               | 4.63 sec: 1.03x faster                                                     |
| logging_simple             | 5.72 us                                                | 5.60 us: 1.02x faster                                                      |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                       |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                       |
| sympy_expand               | 463 ms                                                 | 458 ms: 1.01x faster                                                       |
| sympy_str                  | 275 ms                                                 | 271 ms: 1.01x faster                                                       |
| regex_v8                   | 26.2 ms                                                | 25.9 ms: 1.01x faster                                                      |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.01x faster                                                       |
| mdp                        | 2.72 sec                                               | 2.69 sec: 1.01x faster                                                     |
| typing_runtime_protocols   | 165 us                                                 | 163 us: 1.01x faster                                                       |
| xml_etree_process          | 60.6 ms                                                | 60.2 ms: 1.01x faster                                                      |
| coverage                   | 84.0 ms                                                | 83.4 ms: 1.01x faster                                                      |
| html5lib                   | 64.2 ms                                                | 63.8 ms: 1.01x faster                                                      |
| sqlglot_optimize           | 53.7 ms                                                | 53.5 ms: 1.01x faster                                                      |
| dulwich_log                | 64.3 ms                                                | 64.0 ms: 1.00x faster                                                      |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                       |
| pprint_pformat             | 1.49 sec                                               | 1.50 sec: 1.01x slower                                                     |
| scimark_fft                | 364 ms                                                 | 367 ms: 1.01x slower                                                       |
| create_gc_cycles           | 2.41 ms                                                | 2.43 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 728 ms                                                 | 736 ms: 1.01x slower                                                       |
| raytrace                   | 267 ms                                                 | 270 ms: 1.01x slower                                                       |
| fannkuch                   | 404 ms                                                 | 409 ms: 1.01x slower                                                       |
| python_startup_no_site     | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                      |
| regex_dna                  | 218 ms                                                 | 222 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 1.58 ms                                                | 1.61 ms: 1.02x slower                                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 68.8 ms: 1.02x slower                                                      |
| k_core                     | 2.35 sec                                               | 2.40 sec: 1.02x slower                                                     |
| unpickle_pure_python       | 216 us                                                 | 220 us: 1.02x slower                                                       |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.02x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.02x slower                                                      |
| python_startup             | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                      |
| hexiom                     | 6.16 ms                                                | 6.32 ms: 1.03x slower                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 104 ms: 1.03x slower                                                       |
| spectral_norm              | 115 ms                                                 | 119 ms: 1.03x slower                                                       |
| bench_thread_pool          | 822 us                                                 | 851 us: 1.04x slower                                                       |
| nqueens                    | 78.4 ms                                                | 81.3 ms: 1.04x slower                                                      |
| scimark_lu                 | 113 ms                                                 | 118 ms: 1.04x slower                                                       |
| mako                       | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                      |
| chaos                      | 58.1 ms                                                | 60.7 ms: 1.05x slower                                                      |
| scimark_sor                | 124 ms                                                 | 129 ms: 1.05x slower                                                       |
| coroutines                 | 22.7 ms                                                | 23.8 ms: 1.05x slower                                                      |
| pickle_pure_python         | 310 us                                                 | 330 us: 1.06x slower                                                       |
| logging_silent             | 102 ns                                                 | 108 ns: 1.07x slower                                                       |
| gc_traversal               | 4.37 ms                                                | 4.66 ms: 1.07x slower                                                      |
| nbody                      | 87.0 ms                                                | 94.5 ms: 1.09x slower                                                      |
| json_dumps                 | 10.6 ms                                                | 11.5 ms: 1.09x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (9): connected_components, sphinx, xml_etree_generate, shortest_path, sympy_integrate, docutils, deltablue, asyncio_websockets, float
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241202-3.14.0a2+-07f228b/bm-20241202-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-07f228b.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 99.79% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x