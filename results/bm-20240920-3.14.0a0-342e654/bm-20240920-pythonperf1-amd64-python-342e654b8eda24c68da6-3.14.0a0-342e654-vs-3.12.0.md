# Results vs. 3.12.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-amd64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.015x slower
- HPT reliability: 99.49%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 84.6 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 253 ms: 1.45x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                       |
| async_tree_none            | 291 ms                                                      | 213 ms: 1.37x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 566 ms: 1.36x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 265 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 395 ms: 1.27x faster                                                       |
| async_tree_io              | 731 ms                                                      | 578 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.33x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 55.8 ms: 1.02x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 85.0 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 92.6 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.19 us: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.3 ms: 1.01x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 18.5 us: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 58.0 ms: 1.04x slower                                                      |
| pickle_list          | 2.83 us                                                     | 2.99 us: 1.06x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.16 ms: 1.08x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 41.0 ms: 1.09x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 218 us: 1.11x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| unpickle             | 8.18 us                                                     | 9.51 us: 1.16x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 24.9 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 253 ms: 1.45x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                       |
| async_tree_none            | 291 ms                                                      | 213 ms: 1.37x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 566 ms: 1.36x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 265 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 395 ms: 1.27x faster                                                       |
| async_tree_io              | 731 ms                                                      | 578 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.68 sec: 1.25x faster                                                     |
| deepcopy                   | 238 us                                                      | 193 us: 1.24x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 21.5 us: 1.10x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.94 us: 1.08x faster                                                      |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 75.6 ms: 1.06x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.2 ms: 1.06x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 84.6 ms: 1.06x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 811 us: 1.06x faster                                                       |
| go                         | 91.6 ms                                                     | 87.6 ms: 1.05x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 467 ms: 1.04x faster                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 66.4 ms: 1.04x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.19 us: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 43.2 ms: 1.03x faster                                                      |
| float                      | 56.8 ms                                                     | 55.8 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.3 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.7 ms: 1.01x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 18.5 us: 1.01x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 49.2 ms: 1.02x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.02x slower                                                      |
| chaos                      | 43.3 ms                                                     | 44.2 ms: 1.02x slower                                                      |
| async_generators           | 239 ms                                                      | 245 ms: 1.02x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.42 us: 1.02x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                     |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 64.4 ms: 1.03x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 192 ms: 1.03x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.91 us: 1.03x slower                                                      |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 58.0 ms: 1.04x slower                                                      |
| raytrace                   | 192 ms                                                      | 201 ms: 1.04x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 61.7 ms: 1.05x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 63.4 ns: 1.05x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 78.4 ms: 1.05x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.4 ms: 1.05x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 70.5 ms: 1.05x slower                                                      |
| pickle_list                | 2.83 us                                                     | 2.99 us: 1.06x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 92.6 ms: 1.06x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                     |
| deltablue                  | 2.16 ms                                                     | 2.30 ms: 1.06x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 548 ms: 1.07x slower                                                       |
| pycparser                  | 699 ms                                                      | 747 ms: 1.07x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                     |
| json_dumps                 | 5.70 ms                                                     | 6.16 ms: 1.08x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.9 ms: 1.09x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.46 ms: 1.09x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 41.0 ms: 1.09x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.09x slower                                                      |
| sympy_expand               | 284 ms                                                      | 310 ms: 1.09x slower                                                       |
| pyflate                    | 295 ms                                                      | 322 ms: 1.09x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 218 us: 1.11x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 896 us: 1.11x slower                                                       |
| richards_super             | 32.1 ms                                                     | 36.1 ms: 1.12x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.1 ms: 1.13x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.93 ms: 1.15x slower                                                      |
| scimark_fft                | 184 ms                                                      | 212 ms: 1.15x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 43.1 ns: 1.15x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.6 ms: 1.16x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.58 sec: 1.16x slower                                                     |
| coverage                   | 40.8 ms                                                     | 47.3 ms: 1.16x slower                                                      |
| unpickle                   | 8.18 us                                                     | 9.51 us: 1.16x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.16x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 92.5 ms: 1.17x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 884 us: 1.18x slower                                                       |
| nbody                      | 71.9 ms                                                     | 85.0 ms: 1.18x slower                                                      |
| fannkuch                   | 247 ms                                                      | 300 ms: 1.21x slower                                                       |
| telco                      | 4.13 ms                                                     | 5.39 ms: 1.31x slower                                                      |
| json                       | 3.05 ms                                                     | 4.04 ms: 1.33x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (4): unpickle_list, mako, xml_etree_parse, gc_traversal
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.015x slower
# HPT report

- Reliability score: 99.49% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown