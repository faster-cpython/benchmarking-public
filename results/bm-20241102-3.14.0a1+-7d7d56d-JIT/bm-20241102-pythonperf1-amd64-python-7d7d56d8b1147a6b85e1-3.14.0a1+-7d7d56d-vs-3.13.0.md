# Results vs. 3.13.0

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: windows-amd64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.002x slower
- HPT reliability: 96.01%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 246 ms: 1.11x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.89 sec: 1.20x slower                                                      |
| sphinx         | 633 ms                                                      | 766 ms: 1.21x slower                                                        |
| tornado_http   | 93.0 ms                                                     | 97.1 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 260 ms: 1.11x faster                                                        |
| async_tree_none            | 226 ms                                                      | 209 ms: 1.08x faster                                                        |
| async_tree_memoization     | 276 ms                                                      | 264 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 391 ms: 1.02x slower                                                        |
| async_tree_none_tg         | 209 ms                                                      | 219 ms: 1.05x slower                                                        |
| async_tree_io              | 521 ms                                                      | 555 ms: 1.06x slower                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 401 ms: 1.06x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 14.2 ms: 1.11x slower                                                       |
| async_generators           | 223 ms                                                      | 268 ms: 1.20x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 627 ms: 1.21x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 54.0 ms: 1.27x faster                                                       |
| float          | 49.9 ms                                                     | 46.4 ms: 1.08x faster                                                       |
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.8 ms: 1.45x faster                                                       |
| regex_effbot   | 1.58 ms                                                     | 1.56 ms: 1.01x faster                                                       |
| regex_compile  | 80.5 ms                                                     | 90.8 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.28 sec: 1.09x faster                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 50.2 ms: 1.08x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.5 us: 1.05x faster                                                       |
| xml_etree_process    | 37.0 ms                                                     | 35.6 ms: 1.04x faster                                                       |
| xml_etree_parse      | 93.6 ms                                                     | 92.7 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 61.8 ms                                                     | 62.8 ms: 1.02x slower                                                       |
| json_dumps           | 5.92 ms                                                     | 6.12 ms: 1.03x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 145 us: 1.09x slower                                                        |
| pickle_pure_python   | 190 us                                                      | 206 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 24.1 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 4.97 ms: 1.28x faster                                                       |
| django_template | 22.4 ms                                                     | 26.9 ms: 1.20x slower                                                       |
| genshi_text     | 15.6 ms                                                     | 19.2 ms: 1.23x slower                                                       |
| genshi_xml      | 35.5 ms                                                     | 46.9 ms: 1.32x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 542 us: 16.22x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 14.8 ms: 1.45x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 16.2 us: 1.44x faster                                                       |
| mako                       | 6.35 ms                                                     | 4.97 ms: 1.28x faster                                                       |
| nbody                      | 68.4 ms                                                     | 54.0 ms: 1.27x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 63.5 ms: 1.20x faster                                                       |
| deepcopy                   | 226 us                                                      | 190 us: 1.19x faster                                                        |
| spectral_norm              | 62.8 ms                                                     | 52.8 ms: 1.19x faster                                                       |
| scimark_fft                | 172 ms                                                      | 154 ms: 1.12x faster                                                        |
| crypto_pyaes               | 45.4 ms                                                     | 40.7 ms: 1.12x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.85 us: 1.11x faster                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.20 ms: 1.11x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 260 ms: 1.11x faster                                                        |
| scimark_monte_carlo        | 40.8 ms                                                     | 36.9 ms: 1.11x faster                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.28 sec: 1.09x faster                                                      |
| pprint_pformat             | 999 ms                                                      | 915 ms: 1.09x faster                                                        |
| pprint_safe_repr           | 494 ms                                                      | 453 ms: 1.09x faster                                                        |
| telco                      | 4.79 ms                                                     | 4.40 ms: 1.09x faster                                                       |
| bpe_tokeniser              | 2.91 sec                                                    | 2.68 sec: 1.09x faster                                                      |
| connected_components       | 332 ms                                                      | 307 ms: 1.08x faster                                                        |
| async_tree_none            | 226 ms                                                      | 209 ms: 1.08x faster                                                        |
| xml_etree_generate         | 54.0 ms                                                     | 50.2 ms: 1.08x faster                                                       |
| float                      | 49.9 ms                                                     | 46.4 ms: 1.08x faster                                                       |
| json                       | 3.19 ms                                                     | 3.00 ms: 1.06x faster                                                       |
| shortest_path              | 362 ms                                                      | 342 ms: 1.06x faster                                                        |
| python_startup             | 25.4 ms                                                     | 24.1 ms: 1.06x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.05x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 264 ms: 1.04x faster                                                        |
| xml_etree_process          | 37.0 ms                                                     | 35.6 ms: 1.04x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.91 ms: 1.03x faster                                                       |
| pathlib                    | 80.9 ms                                                     | 78.5 ms: 1.03x faster                                                       |
| fannkuch                   | 253 ms                                                      | 247 ms: 1.03x faster                                                        |
| dulwich_log                | 40.8 ms                                                     | 39.9 ms: 1.02x faster                                                       |
| meteor_contest             | 73.5 ms                                                     | 72.7 ms: 1.01x faster                                                       |
| xml_etree_parse            | 93.6 ms                                                     | 92.7 ms: 1.01x faster                                                       |
| pidigits                   | 148 ms                                                      | 147 ms: 1.01x faster                                                        |
| regex_effbot               | 1.58 ms                                                     | 1.56 ms: 1.01x faster                                                       |
| scimark_lu                 | 53.0 ms                                                     | 53.4 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 62.8 ms: 1.02x slower                                                       |
| coverage                   | 45.6 ms                                                     | 46.4 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 391 ms: 1.02x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 55.8 ns: 1.02x slower                                                       |
| bench_mp_pool              | 86.4 ms                                                     | 88.5 ms: 1.02x slower                                                       |
| json_dumps                 | 5.92 ms                                                     | 6.12 ms: 1.03x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.16 us: 1.03x slower                                                       |
| tornado_http               | 93.0 ms                                                     | 97.1 ms: 1.04x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.56 us: 1.05x slower                                                       |
| async_tree_none_tg         | 209 ms                                                      | 219 ms: 1.05x slower                                                        |
| pyflate                    | 283 ms                                                      | 298 ms: 1.05x slower                                                        |
| go                         | 87.0 ms                                                     | 91.9 ms: 1.06x slower                                                       |
| pycparser                  | 683 ms                                                      | 722 ms: 1.06x slower                                                        |
| async_tree_io              | 521 ms                                                      | 555 ms: 1.06x slower                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 401 ms: 1.06x slower                                                        |
| chaos                      | 38.5 ms                                                     | 41.1 ms: 1.07x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 145 us: 1.09x slower                                                        |
| create_gc_cycles           | 1.26 ms                                                     | 1.37 ms: 1.09x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 206 us: 1.09x slower                                                        |
| mdp                        | 1.39 sec                                                    | 1.52 sec: 1.09x slower                                                      |
| typing_runtime_protocols   | 105 us                                                      | 117 us: 1.11x slower                                                        |
| sympy_expand               | 291 ms                                                      | 323 ms: 1.11x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 14.2 ms: 1.11x slower                                                       |
| 2to3                       | 221 ms                                                      | 246 ms: 1.11x slower                                                        |
| regex_compile              | 80.5 ms                                                     | 90.8 ms: 1.13x slower                                                       |
| sympy_str                  | 169 ms                                                      | 192 ms: 1.14x slower                                                        |
| comprehensions             | 10.3 us                                                     | 11.8 us: 1.15x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 65.5 ms: 1.15x slower                                                       |
| pylint                     | 211 ms                                                      | 244 ms: 1.16x slower                                                        |
| sqlglot_parse              | 771 us                                                      | 893 us: 1.16x slower                                                        |
| generators                 | 19.5 ms                                                     | 22.7 ms: 1.16x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 102 ms: 1.17x slower                                                        |
| async_generators           | 223 ms                                                      | 268 ms: 1.20x slower                                                        |
| docutils                   | 1.57 sec                                                    | 1.89 sec: 1.20x slower                                                      |
| django_template            | 22.4 ms                                                     | 26.9 ms: 1.20x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 210 ms: 1.20x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 627 ms: 1.21x slower                                                        |
| sphinx                     | 633 ms                                                      | 766 ms: 1.21x slower                                                        |
| sqlglot_transpile          | 956 us                                                      | 1.18 ms: 1.23x slower                                                       |
| genshi_text                | 15.6 ms                                                     | 19.2 ms: 1.23x slower                                                       |
| deltablue                  | 1.92 ms                                                     | 2.37 ms: 1.23x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 15.6 ms: 1.25x slower                                                       |
| richards_super             | 30.9 ms                                                     | 38.7 ms: 1.25x slower                                                       |
| richards                   | 27.3 ms                                                     | 34.6 ms: 1.27x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 42.7 ms: 1.30x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 5.14 ms: 1.32x slower                                                       |
| genshi_xml                 | 35.5 ms                                                     | 46.9 ms: 1.32x slower                                                       |
| raytrace                   | 160 ms                                                      | 216 ms: 1.35x slower                                                        |
| k_core                     | 1.74 sec                                                    | 2.43 sec: 1.40x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (5): bench_thread_pool, html5lib, regex_dna, python_startup_no_site, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: sqlite_synth

- Geometric mean (including insignificant results): 1.002x slower
# HPT report

- Reliability score: 96.01% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown