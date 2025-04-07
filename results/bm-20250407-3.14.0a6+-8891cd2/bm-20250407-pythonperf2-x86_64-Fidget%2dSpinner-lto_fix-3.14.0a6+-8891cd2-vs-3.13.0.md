# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: lto_fix
- machine: linux-x86_64
- commit hash: 8891cd2
- commit date: 2025-04-07
- overall geometric mean: 1.074x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 274 ms: 1.07x faster                                                      |
| docutils       | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                    |
| html5lib       | 73.5 ms                                                      | 66.1 ms: 1.11x faster                                                     |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                    |
| Geometric mean | (ref)                                                        | 1.05x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                      |
| async_tree_memoization     | 453 ms                                                       | 332 ms: 1.37x faster                                                      |
| async_tree_io              | 843 ms                                                       | 629 ms: 1.34x faster                                                      |
| async_tree_none            | 376 ms                                                       | 285 ms: 1.32x faster                                                      |
| async_tree_io_tg           | 831 ms                                                       | 631 ms: 1.32x faster                                                      |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                                      |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 504 ms: 1.20x faster                                                      |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 499 ms: 1.16x faster                                                      |
| async_generators           | 457 ms                                                       | 407 ms: 1.12x faster                                                      |
| coroutines                 | 21.6 ms                                                      | 21.6 ms: 1.00x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 68.1 ms: 1.19x faster                                                     |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                      |
| nbody          | 89.3 ms                                                      | 93.4 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                        | 1.04x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.12 ms: 1.18x faster                                                     |
| regex_v8       | 26.1 ms                                                      | 24.4 ms: 1.07x faster                                                     |
| regex_compile  | 143 ms                                                       | 133 ms: 1.07x faster                                                      |
| regex_dna      | 247 ms                                                       | 238 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                        | 1.09x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.06 sec: 1.20x faster                                                    |
| xml_etree_parse      | 150 ms                                                       | 139 ms: 1.08x faster                                                      |
| xml_etree_process    | 61.2 ms                                                      | 58.3 ms: 1.05x faster                                                     |
| xml_etree_iterparse  | 103 ms                                                       | 98.4 ms: 1.04x faster                                                     |
| unpickle_pure_python | 217 us                                                       | 210 us: 1.03x faster                                                      |
| xml_etree_generate   | 86.5 ms                                                      | 84.1 ms: 1.03x faster                                                     |
| json_dumps           | 11.1 ms                                                      | 11.3 ms: 1.01x slower                                                     |
| pickle_pure_python   | 323 us                                                       | 328 us: 1.02x slower                                                      |
| json_loads           | 24.7 us                                                      | 26.7 us: 1.08x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                     |
| python_startup_no_site | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 22.9 ms: 1.15x faster                                                     |
| genshi_xml      | 57.1 ms                                                      | 53.1 ms: 1.08x faster                                                     |
| django_template | 36.4 ms                                                      | 35.8 ms: 1.02x faster                                                     |
| mako            | 10.4 ms                                                      | 11.1 ms: 1.07x slower                                                     |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.30 sec: 1.96x faster                                                    |
| deepcopy                   | 392 us                                                       | 274 us: 1.43x faster                                                      |
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                      |
| deepcopy_memo              | 38.6 us                                                      | 27.9 us: 1.39x faster                                                     |
| async_tree_memoization     | 453 ms                                                       | 332 ms: 1.37x faster                                                      |
| async_tree_io              | 843 ms                                                       | 629 ms: 1.34x faster                                                      |
| async_tree_none            | 376 ms                                                       | 285 ms: 1.32x faster                                                      |
| async_tree_io_tg           | 831 ms                                                       | 631 ms: 1.32x faster                                                      |
| go                         | 162 ms                                                       | 126 ms: 1.28x faster                                                      |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                                      |
| deepcopy_reduce            | 3.54 us                                                      | 2.86 us: 1.24x faster                                                     |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 504 ms: 1.20x faster                                                      |
| tomli_loads                | 2.46 sec                                                     | 2.06 sec: 1.20x faster                                                    |
| pyflate                    | 503 ms                                                       | 421 ms: 1.20x faster                                                      |
| float                      | 81.3 ms                                                      | 68.1 ms: 1.19x faster                                                     |
| scimark_sor                | 123 ms                                                       | 104 ms: 1.18x faster                                                      |
| regex_effbot               | 3.67 ms                                                      | 3.12 ms: 1.18x faster                                                     |
| generators                 | 33.6 ms                                                      | 28.9 ms: 1.17x faster                                                     |
| richards                   | 52.9 ms                                                      | 45.4 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 499 ms: 1.16x faster                                                      |
| richards_super             | 59.6 ms                                                      | 51.5 ms: 1.16x faster                                                     |
| genshi_text                | 26.2 ms                                                      | 22.9 ms: 1.15x faster                                                     |
| telco                      | 8.79 ms                                                      | 7.72 ms: 1.14x faster                                                     |
| scimark_monte_carlo        | 66.1 ms                                                      | 58.3 ms: 1.13x faster                                                     |
| async_generators           | 457 ms                                                       | 407 ms: 1.12x faster                                                      |
| html5lib                   | 73.5 ms                                                      | 66.1 ms: 1.11x faster                                                     |
| dulwich_log                | 68.2 ms                                                      | 62.0 ms: 1.10x faster                                                     |
| pylint                     | 347 ms                                                       | 317 ms: 1.09x faster                                                      |
| scimark_fft                | 328 ms                                                       | 300 ms: 1.09x faster                                                      |
| pprint_safe_repr           | 843 ms                                                       | 773 ms: 1.09x faster                                                      |
| pprint_pformat             | 1.72 sec                                                     | 1.58 sec: 1.09x faster                                                    |
| bpe_tokeniser              | 5.09 sec                                                     | 4.68 sec: 1.09x faster                                                    |
| xml_etree_parse            | 150 ms                                                       | 139 ms: 1.08x faster                                                      |
| spectral_norm              | 97.0 ms                                                      | 89.5 ms: 1.08x faster                                                     |
| genshi_xml                 | 57.1 ms                                                      | 53.1 ms: 1.08x faster                                                     |
| regex_v8                   | 26.1 ms                                                      | 24.4 ms: 1.07x faster                                                     |
| regex_compile              | 143 ms                                                       | 133 ms: 1.07x faster                                                      |
| deltablue                  | 3.42 ms                                                      | 3.19 ms: 1.07x faster                                                     |
| 2to3                       | 293 ms                                                       | 274 ms: 1.07x faster                                                      |
| sympy_integrate            | 23.6 ms                                                      | 22.1 ms: 1.07x faster                                                     |
| logging_silent             | 97.9 ns                                                      | 92.0 ns: 1.06x faster                                                     |
| sympy_expand               | 509 ms                                                       | 484 ms: 1.05x faster                                                      |
| xml_etree_process          | 61.2 ms                                                      | 58.3 ms: 1.05x faster                                                     |
| json                       | 5.69 ms                                                      | 5.44 ms: 1.05x faster                                                     |
| xml_etree_iterparse        | 103 ms                                                       | 98.4 ms: 1.04x faster                                                     |
| hexiom                     | 6.55 ms                                                      | 6.27 ms: 1.04x faster                                                     |
| meteor_contest             | 130 ms                                                       | 124 ms: 1.04x faster                                                      |
| sympy_str                  | 298 ms                                                       | 286 ms: 1.04x faster                                                      |
| pathlib                    | 17.5 ms                                                      | 16.9 ms: 1.04x faster                                                     |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.59 ms: 1.04x faster                                                     |
| scimark_lu                 | 98.7 ms                                                      | 94.9 ms: 1.04x faster                                                     |
| regex_dna                  | 247 ms                                                       | 238 ms: 1.04x faster                                                      |
| unpickle_pure_python       | 217 us                                                       | 210 us: 1.03x faster                                                      |
| xml_etree_generate         | 86.5 ms                                                      | 84.1 ms: 1.03x faster                                                     |
| connected_components       | 432 ms                                                       | 420 ms: 1.03x faster                                                      |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.8 ms: 1.03x faster                                                     |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.03x faster                                                      |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                    |
| k_core                     | 2.17 sec                                                     | 2.11 sec: 1.03x faster                                                    |
| sqlite_synth               | 2.91 us                                                      | 2.83 us: 1.03x faster                                                     |
| shortest_path              | 460 ms                                                       | 450 ms: 1.02x faster                                                      |
| chaos                      | 60.2 ms                                                      | 59.0 ms: 1.02x faster                                                     |
| logging_format             | 6.94 us                                                      | 6.81 us: 1.02x faster                                                     |
| logging_simple             | 6.39 us                                                      | 6.28 us: 1.02x faster                                                     |
| raytrace                   | 273 ms                                                       | 268 ms: 1.02x faster                                                      |
| django_template            | 36.4 ms                                                      | 35.8 ms: 1.02x faster                                                     |
| sqlalchemy_declarative     | 148 ms                                                       | 147 ms: 1.01x faster                                                      |
| coroutines                 | 21.6 ms                                                      | 21.6 ms: 1.00x slower                                                     |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                      |
| docutils                   | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                    |
| json_dumps                 | 11.1 ms                                                      | 11.3 ms: 1.01x slower                                                     |
| pickle_pure_python         | 323 us                                                       | 328 us: 1.02x slower                                                      |
| coverage                   | 80.0 ms                                                      | 81.8 ms: 1.02x slower                                                     |
| python_startup             | 15.9 ms                                                      | 16.4 ms: 1.03x slower                                                     |
| bench_thread_pool          | 942 us                                                       | 974 us: 1.03x slower                                                      |
| nqueens                    | 90.7 ms                                                      | 94.1 ms: 1.04x slower                                                     |
| comprehensions             | 17.0 us                                                      | 17.7 us: 1.04x slower                                                     |
| create_gc_cycles           | 2.68 ms                                                      | 2.80 ms: 1.04x slower                                                     |
| nbody                      | 89.3 ms                                                      | 93.4 ms: 1.05x slower                                                     |
| mako                       | 10.4 ms                                                      | 11.1 ms: 1.07x slower                                                     |
| many_optionals             | 930 us                                                       | 1.00 ms: 1.08x slower                                                     |
| json_loads                 | 24.7 us                                                      | 26.7 us: 1.08x slower                                                     |
| crypto_pyaes               | 73.3 ms                                                      | 79.4 ms: 1.08x slower                                                     |
| python_startup_no_site     | 8.96 ms                                                      | 10.5 ms: 1.17x slower                                                     |
| subparsers                 | 17.5 ms                                                      | 22.3 ms: 1.28x slower                                                     |
| gc_traversal               | 4.74 ms                                                      | 6.58 ms: 1.39x slower                                                     |
| bench_mp_pool              | 5.12 ms                                                      | 1.09 sec: 212.32x slower                                                  |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                              |

Benchmark hidden because not significant (4): pycparser, fannkuch, typing_runtime_protocols, asyncio_websockets
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250407-3.14.0a6+-8891cd2/bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.074x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.04x