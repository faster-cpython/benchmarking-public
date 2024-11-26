# Results vs. 3.13.0

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: windows-amd64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.040x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 225 ms: 1.02x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.69 sec: 1.07x slower                                                      |
| html5lib       | 38.9 ms                                                     | 40.0 ms: 1.03x slower                                                       |
| sphinx         | 633 ms                                                      | 670 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 258 ms: 1.12x faster                                                        |
| asyncio_websockets         | 318 ms                                                      | 304 ms: 1.04x faster                                                        |
| async_tree_none            | 226 ms                                                      | 220 ms: 1.03x faster                                                        |
| coroutines                 | 12.8 ms                                                     | 13.5 ms: 1.06x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 400 ms: 1.06x slower                                                        |
| async_tree_io              | 521 ms                                                      | 566 ms: 1.09x slower                                                        |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 631 ms: 1.22x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 147 ms: 1.00x faster                                                        |
| float          | 49.9 ms                                                     | 54.9 ms: 1.10x slower                                                       |
| nbody          | 68.4 ms                                                     | 79.4 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.6 ms: 1.46x faster                                                       |
| regex_dna      | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| regex_effbot   | 1.58 ms                                                     | 1.56 ms: 1.01x faster                                                       |
| regex_compile  | 80.5 ms                                                     | 92.2 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                       |
| xml_etree_parse      | 93.6 ms                                                     | 95.5 ms: 1.02x slower                                                       |
| xml_etree_iterparse  | 61.8 ms                                                     | 67.6 ms: 1.09x slower                                                       |
| xml_etree_generate   | 54.0 ms                                                     | 59.4 ms: 1.10x slower                                                       |
| xml_etree_process    | 37.0 ms                                                     | 41.2 ms: 1.11x slower                                                       |
| json_dumps           | 5.92 ms                                                     | 6.73 ms: 1.14x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.59 sec: 1.14x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 159 us: 1.19x slower                                                        |
| pickle_pure_python   | 190 us                                                      | 228 us: 1.20x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 23.8 ms: 1.07x faster                                                       |
| python_startup_no_site | 18.1 ms                                                     | 17.8 ms: 1.02x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 36.6 ms: 1.03x slower                                                       |
| mako            | 6.35 ms                                                     | 6.95 ms: 1.09x slower                                                       |
| django_template | 22.4 ms                                                     | 24.9 ms: 1.11x slower                                                       |
| genshi_text     | 15.6 ms                                                     | 17.6 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 531 us: 16.57x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 14.6 ms: 1.46x faster                                                       |
| deepcopy                   | 226 us                                                      | 192 us: 1.18x faster                                                        |
| async_tree_memoization_tg  | 288 ms                                                      | 258 ms: 1.12x faster                                                        |
| deepcopy_memo              | 23.3 us                                                     | 21.5 us: 1.09x faster                                                       |
| python_startup             | 25.4 ms                                                     | 23.8 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.95 us: 1.06x faster                                                       |
| json                       | 3.19 ms                                                     | 3.04 ms: 1.05x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                       |
| asyncio_websockets         | 318 ms                                                      | 304 ms: 1.04x faster                                                        |
| bench_mp_pool              | 86.4 ms                                                     | 83.1 ms: 1.04x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.91 ms: 1.03x faster                                                       |
| async_tree_none            | 226 ms                                                      | 220 ms: 1.03x faster                                                        |
| pathlib                    | 80.9 ms                                                     | 78.9 ms: 1.03x faster                                                       |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| python_startup_no_site     | 18.1 ms                                                     | 17.8 ms: 1.02x faster                                                       |
| connected_components       | 332 ms                                                      | 328 ms: 1.01x faster                                                        |
| regex_effbot               | 1.58 ms                                                     | 1.56 ms: 1.01x faster                                                       |
| shortest_path              | 362 ms                                                      | 360 ms: 1.01x faster                                                        |
| pidigits                   | 148 ms                                                      | 147 ms: 1.00x faster                                                        |
| telco                      | 4.79 ms                                                     | 4.84 ms: 1.01x slower                                                       |
| 2to3                       | 221 ms                                                      | 225 ms: 1.02x slower                                                        |
| xml_etree_parse            | 93.6 ms                                                     | 95.5 ms: 1.02x slower                                                       |
| coverage                   | 45.6 ms                                                     | 46.7 ms: 1.03x slower                                                       |
| html5lib                   | 38.9 ms                                                     | 40.0 ms: 1.03x slower                                                       |
| genshi_xml                 | 35.5 ms                                                     | 36.6 ms: 1.03x slower                                                       |
| go                         | 87.0 ms                                                     | 90.1 ms: 1.04x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 90.2 ms: 1.04x slower                                                       |
| typing_runtime_protocols   | 105 us                                                      | 111 us: 1.05x slower                                                        |
| sympy_expand               | 291 ms                                                      | 306 ms: 1.05x slower                                                        |
| dulwich_log                | 40.8 ms                                                     | 43.0 ms: 1.05x slower                                                       |
| meteor_contest             | 73.5 ms                                                     | 77.5 ms: 1.05x slower                                                       |
| sympy_str                  | 169 ms                                                      | 178 ms: 1.06x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.5 ms: 1.06x slower                                                       |
| sphinx                     | 633 ms                                                      | 670 ms: 1.06x slower                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 400 ms: 1.06x slower                                                        |
| crypto_pyaes               | 45.4 ms                                                     | 48.6 ms: 1.07x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.69 sec: 1.07x slower                                                      |
| pycparser                  | 683 ms                                                      | 734 ms: 1.08x slower                                                        |
| sympy_integrate            | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| bpe_tokeniser              | 2.91 sec                                                    | 3.14 sec: 1.08x slower                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 1.36 ms: 1.08x slower                                                       |
| async_tree_io              | 521 ms                                                      | 566 ms: 1.09x slower                                                        |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                        |
| mdp                        | 1.39 sec                                                    | 1.51 sec: 1.09x slower                                                      |
| logging_simple             | 5.96 us                                                     | 6.50 us: 1.09x slower                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.68 ms: 1.09x slower                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 67.6 ms: 1.09x slower                                                       |
| mako                       | 6.35 ms                                                     | 6.95 ms: 1.09x slower                                                       |
| float                      | 49.9 ms                                                     | 54.9 ms: 1.10x slower                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 59.4 ms: 1.10x slower                                                       |
| django_template            | 22.4 ms                                                     | 24.9 ms: 1.11x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.97 us: 1.11x slower                                                       |
| xml_etree_process          | 37.0 ms                                                     | 41.2 ms: 1.11x slower                                                       |
| pprint_safe_repr           | 494 ms                                                      | 551 ms: 1.12x slower                                                        |
| pprint_pformat             | 999 ms                                                      | 1.12 sec: 1.12x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 17.6 ms: 1.13x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 64.3 ms: 1.13x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 37.3 ms: 1.13x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 198 ms: 1.14x slower                                                        |
| json_dumps                 | 5.92 ms                                                     | 6.73 ms: 1.14x slower                                                       |
| spectral_norm              | 62.8 ms                                                     | 71.6 ms: 1.14x slower                                                       |
| fannkuch                   | 253 ms                                                      | 289 ms: 1.14x slower                                                        |
| tomli_loads                | 1.39 sec                                                    | 1.59 sec: 1.14x slower                                                      |
| pyflate                    | 283 ms                                                      | 324 ms: 1.15x slower                                                        |
| regex_compile              | 80.5 ms                                                     | 92.2 ms: 1.15x slower                                                       |
| chaos                      | 38.5 ms                                                     | 44.3 ms: 1.15x slower                                                       |
| generators                 | 19.5 ms                                                     | 22.5 ms: 1.15x slower                                                       |
| nbody                      | 68.4 ms                                                     | 79.4 ms: 1.16x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 4.60 ms: 1.18x slower                                                       |
| comprehensions             | 10.3 us                                                     | 12.1 us: 1.18x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 159 us: 1.19x slower                                                        |
| scimark_fft                | 172 ms                                                      | 206 ms: 1.20x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 65.6 ns: 1.20x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 228 us: 1.20x slower                                                        |
| sqlglot_transpile          | 956 us                                                      | 1.16 ms: 1.21x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 938 us: 1.22x slower                                                        |
| scimark_lu                 | 53.0 ms                                                     | 64.5 ms: 1.22x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 631 ms: 1.22x slower                                                        |
| deltablue                  | 1.92 ms                                                     | 2.34 ms: 1.22x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 93.0 ms: 1.22x slower                                                       |
| scimark_monte_carlo        | 40.8 ms                                                     | 49.9 ms: 1.22x slower                                                       |
| raytrace                   | 160 ms                                                      | 199 ms: 1.24x slower                                                        |
| richards                   | 27.3 ms                                                     | 34.0 ms: 1.24x slower                                                       |
| richards_super             | 30.9 ms                                                     | 38.5 ms: 1.25x slower                                                       |
| k_core                     | 1.74 sec                                                    | 2.52 sec: 1.45x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (6): bench_thread_pool, async_tree_cpu_io_mixed, tornado_http, async_tree_memoization, async_tree_none_tg, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: sqlite_synth

- Geometric mean (including insignificant results): 1.040x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown