# Results vs. 3.12.0

- fork: python
- ref: 58ce131037ecb34d506a
- machine: windows-amd64
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.00x slower
- HPT reliability: 92.35%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 228 ms: 1.05x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 92.8 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 253 ms: 1.45x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.40x faster                                                       |
| async_tree_none            | 291 ms                                                      | 209 ms: 1.39x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 562 ms: 1.37x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 254 ms: 1.33x faster                                                       |
| async_tree_io              | 731 ms                                                      | 579 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 401 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 390 ms: 1.25x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 56.0 ms: 1.01x faster                                                      |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 85.1 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 89.9 ms: 1.03x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 15.3 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 13.9 us                                                     | 14.0 us: 1.01x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 94.7 ms: 1.02x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 58.2 ms: 1.04x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 209 us: 1.07x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 41.0 ms: 1.09x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.35 ms: 1.11x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.57 sec: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.99 ms: 1.01x faster                                                      |
| django_template | 22.9 ms                                                     | 24.7 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 253 ms: 1.45x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.40x faster                                                       |
| async_tree_none            | 291 ms                                                      | 209 ms: 1.39x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 562 ms: 1.37x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.54 sec: 1.36x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 254 ms: 1.33x faster                                                       |
| deepcopy                   | 238 us                                                      | 184 us: 1.29x faster                                                       |
| async_tree_io              | 731 ms                                                      | 579 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 401 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 390 ms: 1.25x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.19x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 20.1 us: 1.18x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.11x faster                                                      |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                       |
| go                         | 91.6 ms                                                     | 85.4 ms: 1.07x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.1 ms: 1.07x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 819 us: 1.05x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 42.6 ms: 1.04x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 89.3 ms: 1.02x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 79.1 ms: 1.02x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 47.7 ms: 1.02x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.99 ms: 1.01x faster                                                      |
| float                      | 56.8 ms                                                     | 56.0 ms: 1.01x faster                                                      |
| raytrace                   | 192 ms                                                      | 190 ms: 1.01x faster                                                       |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| chaos                      | 43.3 ms                                                     | 43.0 ms: 1.01x faster                                                      |
| async_generators           | 239 ms                                                      | 238 ms: 1.01x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.0 ms: 1.01x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.01x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.33 us: 1.01x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 70.3 ms: 1.02x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 94.7 ms: 1.02x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                     |
| sqlglot_normalize          | 187 ms                                                      | 191 ms: 1.02x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 89.9 ms: 1.03x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.24 ms: 1.04x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 92.8 ms: 1.04x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 77.7 ms: 1.04x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 58.2 ms: 1.04x slower                                                      |
| 2to3                       | 218 ms                                                      | 228 ms: 1.05x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 63.3 ns: 1.05x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.2 ms: 1.05x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.33 ms: 1.06x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 544 ms: 1.06x slower                                                       |
| sympy_expand               | 284 ms                                                      | 301 ms: 1.06x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.07x slower                                                     |
| scimark_lu                 | 58.9 ms                                                     | 63.0 ms: 1.07x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.09 ms: 1.07x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 209 us: 1.07x slower                                                       |
| pyflate                    | 295 ms                                                      | 316 ms: 1.07x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.7 ms: 1.08x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 15.3 ms: 1.08x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 527 ms: 1.08x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 41.0 ms: 1.09x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 879 us: 1.09x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.81 ms: 1.10x slower                                                      |
| scimark_fft                | 184 ms                                                      | 204 ms: 1.11x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.35 ms: 1.11x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 89.4 ms: 1.13x slower                                                      |
| richards_super             | 32.1 ms                                                     | 36.5 ms: 1.14x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.4 ms: 1.14x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.57 sec: 1.15x slower                                                     |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.3 ms: 1.15x slower                                                      |
| coverage                   | 40.8 ms                                                     | 47.0 ms: 1.15x slower                                                      |
| fannkuch                   | 247 ms                                                      | 288 ms: 1.17x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                       |
| nbody                      | 71.9 ms                                                     | 85.1 ms: 1.18x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 911 us: 1.21x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.01 ms: 1.21x slower                                                      |
| pycparser                  | 699 ms                                                      | 870 ms: 1.25x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (7): coroutines, nqueens, sympy_str, xml_etree_iterparse, logging_format, spectral_norm, json
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-58ce131/bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 92.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown