# Results vs. 3.12.0

- fork: python
- ref: 58ce131037ecb34d506a
- machine: windows-amd64
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.02x slower
- HPT reliability: 99.90%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 230 ms: 1.06x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 93.8 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 255 ms: 1.44x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                       |
| async_tree_none            | 291 ms                                                      | 213 ms: 1.37x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 571 ms: 1.35x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                                       |
| async_tree_io              | 731 ms                                                      | 582 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 402 ms: 1.25x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.32x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 89.2 ms: 1.24x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 124 ms: 1.02x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.64 ms: 1.01x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 91.2 ms: 1.04x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 15.6 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 65.8 ms: 1.01x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 94.4 ms: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 59.5 ms: 1.06x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 217 us: 1.11x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 41.9 ms: 1.11x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.16x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.65 sec: 1.20x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.17 ms: 1.01x slower                                                      |
| django_template | 22.9 ms                                                     | 25.0 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 255 ms: 1.44x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                       |
| async_tree_none            | 291 ms                                                      | 213 ms: 1.37x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 571 ms: 1.35x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.59 sec: 1.32x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                                       |
| async_tree_io              | 731 ms                                                      | 582 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 402 ms: 1.25x faster                                                       |
| deepcopy                   | 238 us                                                      | 192 us: 1.24x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.2 us: 1.16x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 21.3 us: 1.11x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.7 ms: 1.09x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.95 us: 1.07x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 819 us: 1.05x faster                                                       |
| go                         | 91.6 ms                                                     | 87.6 ms: 1.04x faster                                                      |
| raytrace                   | 192 ms                                                      | 189 ms: 1.02x faster                                                       |
| regex_dna                  | 126 ms                                                      | 124 ms: 1.02x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 43.5 ms: 1.02x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 79.2 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.77 us: 1.01x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 65.8 ms: 1.01x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.34 us: 1.01x slower                                                      |
| mako                       | 7.09 ms                                                     | 7.17 ms: 1.01x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.64 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 94.4 ms: 1.01x slower                                                      |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                       |
| chaos                      | 43.3 ms                                                     | 44.2 ms: 1.02x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 49.6 ms: 1.02x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.02x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| async_generators           | 239 ms                                                      | 247 ms: 1.03x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 91.2 ms: 1.04x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 195 ms: 1.04x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 69.9 ms: 1.04x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 65.8 ms: 1.05x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 93.8 ms: 1.05x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 78.3 ms: 1.05x slower                                                      |
| 2to3                       | 218 ms                                                      | 230 ms: 1.06x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.30 ms: 1.06x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 59.5 ms: 1.06x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 64.4 ns: 1.07x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 37.0 ms: 1.07x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.0 ms: 1.09x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.09x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 562 ms: 1.10x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.6 ms: 1.10x slower                                                      |
| sympy_expand               | 284 ms                                                      | 311 ms: 1.10x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 64.6 ms: 1.10x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.28 ms: 1.10x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.15 sec: 1.10x slower                                                     |
| hexiom                     | 4.10 ms                                                     | 4.53 ms: 1.10x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 538 ms: 1.10x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 217 us: 1.11x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.14 ms: 1.11x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 41.9 ms: 1.11x slower                                                      |
| pyflate                    | 295 ms                                                      | 329 ms: 1.12x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.89 ms: 1.13x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 913 us: 1.14x slower                                                       |
| python_startup             | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.6 ms: 1.15x slower                                                      |
| richards_super             | 32.1 ms                                                     | 36.9 ms: 1.15x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 110 us: 1.16x slower                                                       |
| scimark_fft                | 184 ms                                                      | 214 ms: 1.16x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.16x slower                                                       |
| pycparser                  | 699 ms                                                      | 824 ms: 1.18x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 52.4 ms: 1.20x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.65 sec: 1.20x slower                                                     |
| coverage                   | 40.8 ms                                                     | 49.4 ms: 1.21x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 913 us: 1.21x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 95.7 ms: 1.21x slower                                                      |
| fannkuch                   | 247 ms                                                      | 303 ms: 1.23x slower                                                       |
| nbody                      | 71.9 ms                                                     | 89.2 ms: 1.24x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.14 ms: 1.25x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (5): json, sympy_sum, bench_mp_pool, coroutines, float
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-58ce131/bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.90% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown