# Results vs. 3.13.0

- fork: python
- ref: v3.13.1
- machine: windows-amd64
- commit hash: 0671451
- commit date: 2024-12-03
- overall geometric mean: 1.004x faster
- HPT reliability: 97.63%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 216 ms: 1.03x faster                                        |
| chameleon      | 4.82 ms                                                     | 4.87 ms: 1.01x slower                                       |
| docutils       | 1.57 sec                                                    | 1.55 sec: 1.02x faster                                      |
| sphinx         | 633 ms                                                      | 618 ms: 1.02x faster                                        |
| tornado_http   | 93.0 ms                                                     | 82.1 ms: 1.13x faster                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 275 ms: 1.05x faster                                        |
| async_tree_none_tg         | 209 ms                                                      | 200 ms: 1.04x faster                                        |
| asyncio_websockets         | 318 ms                                                      | 305 ms: 1.04x faster                                        |
| async_tree_none            | 226 ms                                                      | 221 ms: 1.02x faster                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 386 ms: 1.01x slower                                        |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                        |
| coroutines                 | 12.8 ms                                                     | 13.8 ms: 1.08x slower                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 410 ms: 1.09x slower                                        |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 67.0 ms: 1.02x faster                                       |
| float          | 49.9 ms                                                     | 49.1 ms: 1.02x faster                                       |
| pidigits       | 148 ms                                                      | 146 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                     | 1.45 ms: 1.09x faster                                       |
| regex_compile  | 80.5 ms                                                     | 81.7 ms: 1.01x slower                                       |
| regex_v8       | 21.4 ms                                                     | 25.8 ms: 1.21x slower                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|---------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| tomli_loads         | 1.39 sec                                                    | 1.37 sec: 1.01x faster                                      |
| xml_etree_parse     | 93.6 ms                                                     | 92.4 ms: 1.01x faster                                       |
| xml_etree_iterparse | 61.8 ms                                                     | 62.5 ms: 1.01x slower                                       |
| json_loads          | 15.1 us                                                     | 15.8 us: 1.04x slower                                       |
| json_dumps          | 5.92 ms                                                     | 6.20 ms: 1.05x slower                                       |
| Geometric mean      | (ref)                                                       | 1.01x slower                                                |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_process, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                     | 17.1 ms: 1.06x faster                                       |
| python_startup         | 25.4 ms                                                     | 24.3 ms: 1.05x faster                                       |
| Geometric mean         | (ref)                                                       | 1.05x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 22.4 ms                                                     | 20.5 ms: 1.09x faster                                       |
| genshi_xml      | 35.5 ms                                                     | 33.6 ms: 1.06x faster                                       |
| genshi_text     | 15.6 ms                                                     | 15.7 ms: 1.01x slower                                       |
| mako            | 6.35 ms                                                     | 6.65 ms: 1.05x slower                                       |
| Geometric mean  | (ref)                                                       | 1.02x faster                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| tornado_http               | 93.0 ms                                                     | 82.1 ms: 1.13x faster                                       |
| django_template            | 22.4 ms                                                     | 20.5 ms: 1.09x faster                                       |
| regex_effbot               | 1.58 ms                                                     | 1.45 ms: 1.09x faster                                       |
| pathlib                    | 80.9 ms                                                     | 75.2 ms: 1.08x faster                                       |
| python_startup_no_site     | 18.1 ms                                                     | 17.1 ms: 1.06x faster                                       |
| genshi_xml                 | 35.5 ms                                                     | 33.6 ms: 1.06x faster                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 275 ms: 1.05x faster                                        |
| python_startup             | 25.4 ms                                                     | 24.3 ms: 1.05x faster                                       |
| async_tree_none_tg         | 209 ms                                                      | 200 ms: 1.04x faster                                        |
| asyncio_websockets         | 318 ms                                                      | 305 ms: 1.04x faster                                        |
| meteor_contest             | 73.5 ms                                                     | 70.8 ms: 1.04x faster                                       |
| thrift                     | 8.80 ms                                                     | 8.47 ms: 1.04x faster                                       |
| connected_components       | 332 ms                                                      | 322 ms: 1.03x faster                                        |
| sqlalchemy_imperative      | 9.69 ms                                                     | 9.39 ms: 1.03x faster                                       |
| create_gc_cycles           | 1.26 ms                                                     | 1.22 ms: 1.03x faster                                       |
| shortest_path              | 362 ms                                                      | 352 ms: 1.03x faster                                        |
| k_core                     | 1.74 sec                                                    | 1.69 sec: 1.03x faster                                      |
| 2to3                       | 221 ms                                                      | 216 ms: 1.03x faster                                        |
| bench_mp_pool              | 86.4 ms                                                     | 84.3 ms: 1.02x faster                                       |
| gc_traversal               | 1.97 ms                                                     | 1.92 ms: 1.02x faster                                       |
| sphinx                     | 633 ms                                                      | 618 ms: 1.02x faster                                        |
| async_tree_none            | 226 ms                                                      | 221 ms: 1.02x faster                                        |
| nbody                      | 68.4 ms                                                     | 67.0 ms: 1.02x faster                                       |
| logging_simple             | 5.96 us                                                     | 5.84 us: 1.02x faster                                       |
| typing_runtime_protocols   | 105 us                                                      | 104 us: 1.02x faster                                        |
| float                      | 49.9 ms                                                     | 49.1 ms: 1.02x faster                                       |
| logging_silent             | 54.6 ns                                                     | 53.7 ns: 1.02x faster                                       |
| chaos                      | 38.5 ms                                                     | 37.9 ms: 1.02x faster                                       |
| docutils                   | 1.57 sec                                                    | 1.55 sec: 1.02x faster                                      |
| sympy_expand               | 291 ms                                                      | 287 ms: 1.02x faster                                        |
| bpe_tokeniser              | 2.91 sec                                                    | 2.87 sec: 1.01x faster                                      |
| tomli_loads                | 1.39 sec                                                    | 1.37 sec: 1.01x faster                                      |
| raytrace                   | 160 ms                                                      | 158 ms: 1.01x faster                                        |
| xml_etree_parse            | 93.6 ms                                                     | 92.4 ms: 1.01x faster                                       |
| sympy_integrate            | 12.5 ms                                                     | 12.4 ms: 1.01x faster                                       |
| pidigits                   | 148 ms                                                      | 146 ms: 1.01x faster                                        |
| coverage                   | 45.6 ms                                                     | 45.1 ms: 1.01x faster                                       |
| sympy_sum                  | 86.9 ms                                                     | 86.0 ms: 1.01x faster                                       |
| dulwich_log                | 40.8 ms                                                     | 40.4 ms: 1.01x faster                                       |
| richards                   | 27.3 ms                                                     | 27.1 ms: 1.01x faster                                       |
| logging_format             | 6.26 us                                                     | 6.21 us: 1.01x faster                                       |
| richards_super             | 30.9 ms                                                     | 30.7 ms: 1.01x faster                                       |
| sympy_str                  | 169 ms                                                      | 168 ms: 1.01x faster                                        |
| crypto_pyaes               | 45.4 ms                                                     | 45.2 ms: 1.01x faster                                       |
| sqlalchemy_declarative     | 79.2 ms                                                     | 78.8 ms: 1.00x faster                                       |
| fannkuch                   | 253 ms                                                      | 254 ms: 1.00x slower                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 386 ms: 1.01x slower                                        |
| deltablue                  | 1.92 ms                                                     | 1.93 ms: 1.01x slower                                       |
| genshi_text                | 15.6 ms                                                     | 15.7 ms: 1.01x slower                                       |
| pyflate                    | 283 ms                                                      | 286 ms: 1.01x slower                                        |
| pprint_pformat             | 999 ms                                                      | 1.01 sec: 1.01x slower                                      |
| sqlglot_transpile          | 956 us                                                      | 966 us: 1.01x slower                                        |
| chameleon                  | 4.82 ms                                                     | 4.87 ms: 1.01x slower                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 62.5 ms: 1.01x slower                                       |
| nqueens                    | 56.7 ms                                                     | 57.3 ms: 1.01x slower                                       |
| scimark_fft                | 172 ms                                                      | 174 ms: 1.01x slower                                        |
| deepcopy_memo              | 23.3 us                                                     | 23.6 us: 1.01x slower                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.49 ms: 1.01x slower                                       |
| scimark_monte_carlo        | 40.8 ms                                                     | 41.4 ms: 1.01x slower                                       |
| regex_compile              | 80.5 ms                                                     | 81.7 ms: 1.01x slower                                       |
| deepcopy                   | 226 us                                                      | 230 us: 1.01x slower                                        |
| deepcopy_reduce            | 2.06 us                                                     | 2.09 us: 1.02x slower                                       |
| mdp                        | 1.39 sec                                                    | 1.41 sec: 1.02x slower                                      |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                        |
| scimark_sor                | 76.2 ms                                                     | 78.3 ms: 1.03x slower                                       |
| telco                      | 4.79 ms                                                     | 4.94 ms: 1.03x slower                                       |
| gevent_hub                 | 0.66 ns                                                     | 0.69 ns: 1.04x slower                                       |
| comprehensions             | 10.3 us                                                     | 10.7 us: 1.04x slower                                       |
| json_loads                 | 15.1 us                                                     | 15.8 us: 1.04x slower                                       |
| spectral_norm              | 62.8 ms                                                     | 65.5 ms: 1.04x slower                                       |
| mako                       | 6.35 ms                                                     | 6.65 ms: 1.05x slower                                       |
| json_dumps                 | 5.92 ms                                                     | 6.20 ms: 1.05x slower                                       |
| coroutines                 | 12.8 ms                                                     | 13.8 ms: 1.08x slower                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 410 ms: 1.09x slower                                        |
| scimark_lu                 | 53.0 ms                                                     | 58.3 ms: 1.10x slower                                       |
| regex_v8                   | 21.4 ms                                                     | 25.8 ms: 1.21x slower                                       |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                |

Benchmark hidden because not significant (20): async_tree_memoization, pylint, async_tree_io, html5lib, go, unpickle_pure_python, xml_etree_process, json, bench_thread_pool, sqlglot_parse, regex_dna, xml_etree_generate, generators, pprint_safe_repr, pickle_pure_python, sqlglot_normalize, pycparser, hexiom, sqlglot_optimize, async_tree_io_tg
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: mypy2
Ignored benchmarks (4) of results/bm-20241203-3.13.1-0671451/bm-20241203-pythonperf1-amd64-python-v3.13.1-3.13.1-0671451.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 97.63% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown