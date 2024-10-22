# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mcmodel
- machine: windows-amd64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.05x faster
- HPT reliability: 90.66%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 234 ms: 1.07x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.78 sec: 1.07x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 85.4 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 190 ms: 1.50x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 245 ms: 1.50x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 530 ms: 1.46x faster                                                       |
| async_tree_none            | 291 ms                                                      | 208 ms: 1.40x faster                                                       |
| async_tree_io              | 731 ms                                                      | 543 ms: 1.35x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 256 ms: 1.33x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 382 ms: 1.28x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.39x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 51.1 ms: 1.41x faster                                                      |
| float          | 56.8 ms                                                     | 45.1 ms: 1.26x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 90.2 ms: 1.03x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 23.9 ms: 1.68x slower                                                      |
| Geometric mean | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 179 us: 1.09x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 52.8 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.1 ms: 1.05x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 134 us: 1.01x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 5.78 ms: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.1 ms: 1.05x slower                                                      |
| python_startup         | 19.5 ms                                                     | 20.9 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.18 ms: 1.37x faster                                                      |
| django_template | 22.9 ms                                                     | 26.3 ms: 1.15x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 15.6 us: 1.52x faster                                                      |
| async_tree_none_tg         | 285 ms                                                      | 190 ms: 1.50x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 245 ms: 1.50x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.42 sec: 1.48x faster                                                     |
| spectral_norm              | 66.9 ms                                                     | 45.8 ms: 1.46x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 530 ms: 1.46x faster                                                       |
| nbody                      | 71.9 ms                                                     | 51.1 ms: 1.41x faster                                                      |
| async_tree_none            | 291 ms                                                      | 208 ms: 1.40x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.38x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.18 ms: 1.37x faster                                                      |
| async_tree_io              | 731 ms                                                      | 543 ms: 1.35x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 256 ms: 1.33x faster                                                       |
| deepcopy                   | 238 us                                                      | 180 us: 1.32x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 382 ms: 1.28x faster                                                       |
| float                      | 56.8 ms                                                     | 45.1 ms: 1.26x faster                                                      |
| scimark_fft                | 184 ms                                                      | 151 ms: 1.22x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 40.8 ms: 1.19x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.17 ms: 1.18x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.17x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.1 ms: 1.15x faster                                                      |
| pyflate                    | 295 ms                                                      | 260 ms: 1.13x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 462 ms: 1.11x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 947 ms: 1.10x faster                                                       |
| fannkuch                   | 247 ms                                                      | 225 ms: 1.10x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 179 us: 1.09x faster                                                       |
| chaos                      | 43.3 ms                                                     | 40.0 ms: 1.08x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.80 us: 1.08x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 74.9 ms: 1.07x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.27 us: 1.07x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                     |
| bench_thread_pool          | 857 us                                                      | 808 us: 1.06x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 52.8 ms: 1.06x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 57.3 ns: 1.06x faster                                                      |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.1 ms: 1.05x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 85.4 ms: 1.05x faster                                                      |
| raytrace                   | 192 ms                                                      | 185 ms: 1.04x faster                                                       |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.9 ms: 1.01x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 74.1 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 134 us: 1.01x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 815 us: 1.01x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.78 ms: 1.01x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.04 ms: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 94.0 ms: 1.03x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 90.2 ms: 1.03x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 193 ms: 1.03x slower                                                       |
| sympy_str                  | 175 ms                                                      | 184 ms: 1.05x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.1 ms: 1.05x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.4 ms: 1.05x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                                     |
| go                         | 91.6 ms                                                     | 97.7 ms: 1.07x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.78 sec: 1.07x slower                                                     |
| python_startup             | 19.5 ms                                                     | 20.9 ms: 1.07x slower                                                      |
| 2to3                       | 218 ms                                                      | 234 ms: 1.07x slower                                                       |
| richards                   | 28.4 ms                                                     | 30.6 ms: 1.08x slower                                                      |
| async_generators           | 239 ms                                                      | 259 ms: 1.08x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 14.0 ms: 1.08x slower                                                      |
| richards_super             | 32.1 ms                                                     | 34.8 ms: 1.09x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.35 ms: 1.09x slower                                                      |
| generators                 | 22.5 ms                                                     | 25.0 ms: 1.11x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.61 ms: 1.12x slower                                                      |
| sympy_expand               | 284 ms                                                      | 319 ms: 1.12x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.3 ms: 1.15x slower                                                      |
| pycparser                  | 699 ms                                                      | 804 ms: 1.15x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 91.6 ms: 1.16x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                       |
| coverage                   | 40.8 ms                                                     | 48.5 ms: 1.19x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 900 us: 1.20x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.95 ms: 1.20x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 77.0 ms: 1.31x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 23.9 ms: 1.68x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (5): asyncio_tcp, coroutines, bench_mp_pool, xml_etree_parse, json
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240714-3.14.0a0-d19b26c-JIT/bm-20240714-pythonperf1-amd64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 90.66% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown