# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache_rwx
- machine: windows-amd64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.021x faster
- HPT reliability: 95.08%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 234 ms: 1.06x slower                                                     |
| docutils       | 1.57 sec                                                    | 1.81 sec: 1.15x slower                                                   |
| sphinx         | 633 ms                                                      | 709 ms: 1.12x slower                                                     |
| tornado_http   | 93.0 ms                                                     | 98.5 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                       | 1.08x slower                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 264 ms: 1.09x faster                                                     |
| async_tree_none            | 226 ms                                                      | 219 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 400 ms: 1.06x slower                                                     |
| async_tree_io              | 521 ms                                                      | 565 ms: 1.08x slower                                                     |
| coroutines                 | 12.8 ms                                                     | 13.9 ms: 1.09x slower                                                    |
| async_generators           | 223 ms                                                      | 267 ms: 1.20x slower                                                     |
| async_tree_io_tg           | 518 ms                                                      | 632 ms: 1.22x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                             |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 53.1 ms: 1.29x faster                                                    |
| float          | 49.9 ms                                                     | 48.0 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                       | 1.10x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.0 ms: 1.42x faster                                                    |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                                     |
| regex_effbot   | 1.58 ms                                                     | 1.60 ms: 1.02x slower                                                    |
| regex_compile  | 80.5 ms                                                     | 82.6 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                       | 1.08x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.27 sec: 1.09x faster                                                   |
| xml_etree_generate   | 54.0 ms                                                     | 50.5 ms: 1.07x faster                                                    |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                    |
| xml_etree_process    | 37.0 ms                                                     | 35.3 ms: 1.05x faster                                                    |
| xml_etree_iterparse  | 61.8 ms                                                     | 63.4 ms: 1.03x slower                                                    |
| pickle_pure_python   | 190 us                                                      | 197 us: 1.04x slower                                                     |
| json_dumps           | 5.92 ms                                                     | 6.20 ms: 1.05x slower                                                    |
| unpickle_pure_python | 133 us                                                      | 141 us: 1.05x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 24.2 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                       | 1.02x faster                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.09 ms: 1.25x faster                                                    |
| genshi_xml      | 35.5 ms                                                     | 40.3 ms: 1.14x slower                                                    |
| genshi_text     | 15.6 ms                                                     | 18.5 ms: 1.19x slower                                                    |
| django_template | 22.4 ms                                                     | 26.6 ms: 1.19x slower                                                    |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 531 us: 16.56x faster                                                    |
| deepcopy_memo              | 23.3 us                                                     | 16.2 us: 1.44x faster                                                    |
| regex_v8                   | 21.4 ms                                                     | 15.0 ms: 1.42x faster                                                    |
| nbody                      | 68.4 ms                                                     | 53.1 ms: 1.29x faster                                                    |
| mako                       | 6.35 ms                                                     | 5.09 ms: 1.25x faster                                                    |
| deepcopy                   | 226 us                                                      | 187 us: 1.21x faster                                                     |
| scimark_sor                | 76.2 ms                                                     | 63.1 ms: 1.21x faster                                                    |
| fannkuch                   | 253 ms                                                      | 213 ms: 1.19x faster                                                     |
| spectral_norm              | 62.8 ms                                                     | 53.2 ms: 1.18x faster                                                    |
| crypto_pyaes               | 45.4 ms                                                     | 39.7 ms: 1.14x faster                                                    |
| scimark_monte_carlo        | 40.8 ms                                                     | 35.8 ms: 1.14x faster                                                    |
| pprint_safe_repr           | 494 ms                                                      | 442 ms: 1.12x faster                                                     |
| deepcopy_reduce            | 2.06 us                                                     | 1.85 us: 1.11x faster                                                    |
| pprint_pformat             | 999 ms                                                      | 900 ms: 1.11x faster                                                     |
| scimark_fft                | 172 ms                                                      | 156 ms: 1.11x faster                                                     |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.24 ms: 1.10x faster                                                    |
| tomli_loads                | 1.39 sec                                                    | 1.27 sec: 1.09x faster                                                   |
| async_tree_memoization_tg  | 288 ms                                                      | 264 ms: 1.09x faster                                                     |
| json                       | 3.19 ms                                                     | 2.95 ms: 1.08x faster                                                    |
| xml_etree_generate         | 54.0 ms                                                     | 50.5 ms: 1.07x faster                                                    |
| telco                      | 4.79 ms                                                     | 4.51 ms: 1.06x faster                                                    |
| go                         | 87.0 ms                                                     | 82.4 ms: 1.06x faster                                                    |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                    |
| meteor_contest             | 73.5 ms                                                     | 70.0 ms: 1.05x faster                                                    |
| python_startup             | 25.4 ms                                                     | 24.2 ms: 1.05x faster                                                    |
| xml_etree_process          | 37.0 ms                                                     | 35.3 ms: 1.05x faster                                                    |
| float                      | 49.9 ms                                                     | 48.0 ms: 1.04x faster                                                    |
| async_tree_none            | 226 ms                                                      | 219 ms: 1.03x faster                                                     |
| pyflate                    | 283 ms                                                      | 276 ms: 1.03x faster                                                     |
| dulwich_log                | 40.8 ms                                                     | 40.3 ms: 1.01x faster                                                    |
| scimark_lu                 | 53.0 ms                                                     | 53.3 ms: 1.01x slower                                                    |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.01x slower                                                     |
| bench_mp_pool              | 86.4 ms                                                     | 87.2 ms: 1.01x slower                                                    |
| regex_effbot               | 1.58 ms                                                     | 1.60 ms: 1.02x slower                                                    |
| logging_simple             | 5.96 us                                                     | 6.08 us: 1.02x slower                                                    |
| regex_compile              | 80.5 ms                                                     | 82.6 ms: 1.03x slower                                                    |
| xml_etree_iterparse        | 61.8 ms                                                     | 63.4 ms: 1.03x slower                                                    |
| chaos                      | 38.5 ms                                                     | 39.7 ms: 1.03x slower                                                    |
| pycparser                  | 683 ms                                                      | 707 ms: 1.04x slower                                                     |
| pickle_pure_python         | 190 us                                                      | 197 us: 1.04x slower                                                     |
| json_dumps                 | 5.92 ms                                                     | 6.20 ms: 1.05x slower                                                    |
| logging_format             | 6.26 us                                                     | 6.58 us: 1.05x slower                                                    |
| unpickle_pure_python       | 133 us                                                      | 141 us: 1.05x slower                                                     |
| 2to3                       | 221 ms                                                      | 234 ms: 1.06x slower                                                     |
| sympy_expand               | 291 ms                                                      | 308 ms: 1.06x slower                                                     |
| tornado_http               | 93.0 ms                                                     | 98.5 ms: 1.06x slower                                                    |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 400 ms: 1.06x slower                                                     |
| mdp                        | 1.39 sec                                                    | 1.48 sec: 1.06x slower                                                   |
| comprehensions             | 10.3 us                                                     | 10.9 us: 1.07x slower                                                    |
| sympy_str                  | 169 ms                                                      | 180 ms: 1.07x slower                                                     |
| async_tree_io              | 521 ms                                                      | 565 ms: 1.08x slower                                                     |
| coroutines                 | 12.8 ms                                                     | 13.9 ms: 1.09x slower                                                    |
| coverage                   | 45.6 ms                                                     | 49.5 ms: 1.09x slower                                                    |
| generators                 | 19.5 ms                                                     | 21.2 ms: 1.09x slower                                                    |
| typing_runtime_protocols   | 105 us                                                      | 115 us: 1.09x slower                                                     |
| hexiom                     | 3.89 ms                                                     | 4.25 ms: 1.09x slower                                                    |
| sympy_sum                  | 86.9 ms                                                     | 95.5 ms: 1.10x slower                                                    |
| nqueens                    | 56.7 ms                                                     | 62.7 ms: 1.11x slower                                                    |
| sqlglot_parse              | 771 us                                                      | 858 us: 1.11x slower                                                     |
| create_gc_cycles           | 1.26 ms                                                     | 1.41 ms: 1.12x slower                                                    |
| sphinx                     | 633 ms                                                      | 709 ms: 1.12x slower                                                     |
| genshi_xml                 | 35.5 ms                                                     | 40.3 ms: 1.14x slower                                                    |
| docutils                   | 1.57 sec                                                    | 1.81 sec: 1.15x slower                                                   |
| sqlglot_normalize          | 175 ms                                                      | 202 ms: 1.16x slower                                                     |
| richards_super             | 30.9 ms                                                     | 36.2 ms: 1.17x slower                                                    |
| richards                   | 27.3 ms                                                     | 32.0 ms: 1.17x slower                                                    |
| sqlglot_transpile          | 956 us                                                      | 1.12 ms: 1.17x slower                                                    |
| sqlglot_optimize           | 32.9 ms                                                     | 38.8 ms: 1.18x slower                                                    |
| deltablue                  | 1.92 ms                                                     | 2.27 ms: 1.18x slower                                                    |
| sympy_integrate            | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                                    |
| genshi_text                | 15.6 ms                                                     | 18.5 ms: 1.19x slower                                                    |
| django_template            | 22.4 ms                                                     | 26.6 ms: 1.19x slower                                                    |
| async_generators           | 223 ms                                                      | 267 ms: 1.20x slower                                                     |
| async_tree_io_tg           | 518 ms                                                      | 632 ms: 1.22x slower                                                     |
| pylint                     | 211 ms                                                      | 258 ms: 1.22x slower                                                     |
| raytrace                   | 160 ms                                                      | 206 ms: 1.29x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                             |

Benchmark hidden because not significant (11): bench_thread_pool, gc_traversal, html5lib, logging_silent, pidigits, python_startup_no_site, pathlib, async_tree_none_tg, xml_etree_parse, async_tree_cpu_io_mixed, async_tree_memoization
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.021x faster
# HPT report

- Reliability score: 95.08% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown