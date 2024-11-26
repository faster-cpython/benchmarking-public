# Results vs. 3.12.0

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: windows-amd64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.020x faster
- HPT reliability: 75.17%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 246 ms: 1.13x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.89 sec: 1.14x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 97.1 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 260 ms: 1.41x faster                                                        |
| async_tree_none            | 291 ms                                                      | 209 ms: 1.39x faster                                                        |
| async_tree_io              | 731 ms                                                      | 555 ms: 1.32x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 219 ms: 1.30x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 401 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 627 ms: 1.23x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 54.0 ms: 1.33x faster                                                       |
| float          | 56.8 ms                                                     | 46.4 ms: 1.22x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 90.8 ms: 1.04x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 50.2 ms: 1.11x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.6 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.8 ms: 1.04x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 206 us: 1.06x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.12 ms: 1.07x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 145 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                       |
| python_startup         | 19.5 ms                                                     | 24.1 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 4.97 ms: 1.42x faster                                                       |
| django_template | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 16.2 us: 1.46x faster                                                       |
| mako                       | 7.09 ms                                                     | 4.97 ms: 1.42x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 260 ms: 1.41x faster                                                        |
| async_tree_none            | 291 ms                                                      | 209 ms: 1.39x faster                                                        |
| nbody                      | 71.9 ms                                                     | 54.0 ms: 1.33x faster                                                       |
| async_tree_io              | 731 ms                                                      | 555 ms: 1.32x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 219 ms: 1.30x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.28x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 52.8 ms: 1.27x faster                                                       |
| deepcopy                   | 238 us                                                      | 190 us: 1.25x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 401 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 391 ms: 1.25x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 63.5 ms: 1.24x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 627 ms: 1.23x faster                                                        |
| float                      | 56.8 ms                                                     | 46.4 ms: 1.22x faster                                                       |
| scimark_fft                | 184 ms                                                      | 154 ms: 1.20x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.20x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 40.7 ms: 1.19x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 36.9 ms: 1.19x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.20 ms: 1.16x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 915 ms: 1.14x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 453 ms: 1.13x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.85 us: 1.13x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 50.2 ms: 1.11x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 39.9 ms: 1.11x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 53.4 ms: 1.10x faster                                                       |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 55.8 ns: 1.08x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.6 ms: 1.06x faster                                                       |
| chaos                      | 43.3 ms                                                     | 41.1 ms: 1.05x faster                                                       |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.8 ms: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 72.7 ms: 1.03x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 78.5 ms: 1.03x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.56 us: 1.02x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.16 us: 1.02x faster                                                       |
| json                       | 3.05 ms                                                     | 3.00 ms: 1.02x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 14.2 ms: 1.01x faster                                                       |
| generators                 | 22.5 ms                                                     | 22.7 ms: 1.01x slower                                                       |
| pyflate                    | 295 ms                                                      | 298 ms: 1.01x slower                                                        |
| pycparser                  | 699 ms                                                      | 722 ms: 1.03x slower                                                        |
| regex_compile              | 87.5 ms                                                     | 90.8 ms: 1.04x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 65.5 ms: 1.04x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 206 us: 1.06x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.40 ms: 1.07x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.12 ms: 1.07x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 97.1 ms: 1.08x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 145 us: 1.09x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.37 ms: 1.10x slower                                                       |
| sympy_str                  | 175 ms                                                      | 192 ms: 1.10x slower                                                        |
| mdp                        | 1.37 sec                                                    | 1.52 sec: 1.10x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 893 us: 1.11x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 102 ms: 1.12x slower                                                        |
| async_generators           | 239 ms                                                      | 268 ms: 1.12x slower                                                        |
| raytrace                   | 192 ms                                                      | 216 ms: 1.12x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 210 ms: 1.13x slower                                                        |
| 2to3                       | 218 ms                                                      | 246 ms: 1.13x slower                                                        |
| coverage                   | 40.8 ms                                                     | 46.4 ms: 1.14x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.89 sec: 1.14x slower                                                      |
| sympy_expand               | 284 ms                                                      | 323 ms: 1.14x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.18 ms: 1.15x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                       |
| richards_super             | 32.1 ms                                                     | 38.7 ms: 1.20x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 15.6 ms: 1.21x slower                                                       |
| richards                   | 28.4 ms                                                     | 34.6 ms: 1.22x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 117 us: 1.23x slower                                                        |
| python_startup             | 19.5 ms                                                     | 24.1 ms: 1.24x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 42.7 ms: 1.24x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.91 ms: 1.25x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.14 ms: 1.25x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.5 ms: 1.28x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.37 ms: 1.82x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (4): bench_thread_pool, xml_etree_parse, fannkuch, go
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.020x faster
# HPT report

- Reliability score: 75.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown