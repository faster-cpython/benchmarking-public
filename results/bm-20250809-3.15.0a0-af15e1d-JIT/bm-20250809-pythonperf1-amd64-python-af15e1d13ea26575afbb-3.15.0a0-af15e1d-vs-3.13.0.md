# Results vs. 3.13.0

- fork: python
- ref: af15e1d13ea26575afbb
- machine: windows-amd64
- commit hash: af15e1d
- commit date: 2025-08-09
- overall geometric mean: 1.079x faster
- HPT reliability: 91.42%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.04x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                     |
| html5lib       | 38.2 ms                                                     | 40.1 ms: 1.05x slower                                                      |
| sphinx         | 617 ms                                                      | 650 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| async_tree_io              | 513 ms                                                      | 389 ms: 1.32x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 387 ms: 1.28x faster                                                       |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.14x faster                                                       |
| async_generators           | 223 ms                                                      | 250 ms: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.18x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 52.8 ms: 1.25x faster                                                      |
| float          | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.7 ms: 1.74x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.59 ms: 1.07x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 77.7 ms: 1.04x faster                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 105 us: 1.24x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.39 ms: 1.15x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 51.1 ms: 1.05x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 35.7 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.2 ms: 1.04x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 204 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.8 ms: 1.10x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.9 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.38 ms: 1.22x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.6 ms: 1.02x slower                                                      |
| genshi_xml      | 33.9 ms                                                     | 35.0 ms: 1.03x slower                                                      |
| django_template | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 496 us: 17.06x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 32.1 ms: 2.35x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                       |
| mdp                        | 1.43 sec                                                    | 800 ms: 1.79x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.7 ms: 1.74x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| deepcopy                   | 223 us                                                      | 169 us: 1.32x faster                                                       |
| async_tree_io              | 513 ms                                                      | 389 ms: 1.32x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 387 ms: 1.28x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.1 us: 1.28x faster                                                      |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                     |
| nbody                      | 66.3 ms                                                     | 52.8 ms: 1.25x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 105 us: 1.24x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.38 ms: 1.22x faster                                                      |
| fannkuch                   | 252 ms                                                      | 209 ms: 1.20x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                       |
| scimark_fft                | 175 ms                                                      | 151 ms: 1.16x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.49 sec: 1.15x faster                                                     |
| json_dumps                 | 6.19 ms                                                     | 5.39 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.14x faster                                                       |
| float                      | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                                      |
| go                         | 84.7 ms                                                     | 75.7 ms: 1.12x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.33 ms: 1.12x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.82 us: 1.11x faster                                                      |
| pprint_safe_repr           | 485 ms                                                      | 440 ms: 1.10x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 893 ms: 1.09x faster                                                       |
| pyflate                    | 283 ms                                                      | 263 ms: 1.08x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.59 ms: 1.07x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| json                       | 3.30 ms                                                     | 3.10 ms: 1.06x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 51.1 ms: 1.05x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.63 sec: 1.04x faster                                                     |
| regex_compile              | 80.7 ms                                                     | 77.7 ms: 1.04x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 74.5 ms: 1.02x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 35.7 ms: 1.02x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.75 ms: 1.02x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 71.6 ms: 1.00x faster                                                      |
| scimark_lu                 | 56.7 ms                                                     | 57.2 ms: 1.01x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 55.3 ns: 1.01x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 46.3 ms: 1.02x slower                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.61 us: 1.02x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 40.9 ms: 1.02x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.6 ms: 1.02x slower                                                      |
| sympy_expand               | 286 ms                                                      | 292 ms: 1.02x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.6 ms: 1.02x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.6 us: 1.02x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 87.5 ms: 1.03x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.7 ms: 1.03x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 35.0 ms: 1.03x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.8 ms: 1.03x slower                                                      |
| sympy_str                  | 167 ms                                                      | 173 ms: 1.04x slower                                                       |
| 2to3                       | 215 ms                                                      | 223 ms: 1.04x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.7 ms: 1.04x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.3 ms: 1.04x slower                                                      |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.43 us: 1.04x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 66.2 ms: 1.04x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.2 ms: 1.04x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.04 us: 1.05x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 40.1 ms: 1.05x slower                                                      |
| sphinx                     | 617 ms                                                      | 650 ms: 1.05x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.06 ms: 1.06x slower                                                      |
| chaos                      | 37.9 ms                                                     | 40.3 ms: 1.06x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 59.9 ms: 1.07x slower                                                      |
| coverage                   | 45.3 ms                                                     | 48.5 ms: 1.07x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                     |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.09x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 204 us: 1.10x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.8 ms: 1.10x slower                                                      |
| async_generators           | 223 ms                                                      | 250 ms: 1.12x slower                                                       |
| raytrace                   | 153 ms                                                      | 174 ms: 1.14x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.9 ms: 1.18x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.18x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.26 ms: 1.20x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                      |
| many_optionals             | 361 us                                                      | 571 us: 1.58x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 29.8 ms: 2.75x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (6): pylint, shortest_path, pycparser, typing_runtime_protocols, connected_components, pidigits
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250809-3.15.0a0-af15e1d-JIT/bm-20250809-pythonperf1-amd64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.079x faster

# HPT report

- Reliability score: 91.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown