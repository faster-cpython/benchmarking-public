# Results vs. 3.12.0

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: windows-amd64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.04x faster
- HPT reliability: 89.56%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 237 ms: 1.09x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 84.3 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 246 ms: 1.49x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 192 ms: 1.49x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 530 ms: 1.45x faster                                                       |
| async_tree_none            | 291 ms                                                      | 212 ms: 1.38x faster                                                       |
| async_tree_io              | 731 ms                                                      | 544 ms: 1.34x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 256 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.38x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 51.4 ms: 1.40x faster                                                      |
| float          | 56.8 ms                                                     | 45.6 ms: 1.25x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 121 ms: 1.05x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 90.1 ms: 1.03x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 20.1 ms: 1.41x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 180 us: 1.08x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.29 sec: 1.06x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 53.8 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 5.89 ms: 1.03x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 39.2 ms: 1.04x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 97.6 ms: 1.05x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 142 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.6 ms: 1.14x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.5 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.19 ms: 1.37x faster                                                      |
| django_template | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 15.8 us: 1.50x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 246 ms: 1.49x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 192 ms: 1.49x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 45.3 ms: 1.48x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 530 ms: 1.45x faster                                                       |
| nbody                      | 71.9 ms                                                     | 51.4 ms: 1.40x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.52 sec: 1.38x faster                                                     |
| async_tree_none            | 291 ms                                                      | 212 ms: 1.38x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.19 ms: 1.37x faster                                                      |
| async_tree_io              | 731 ms                                                      | 544 ms: 1.34x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.34x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 256 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                       |
| deepcopy                   | 238 us                                                      | 184 us: 1.29x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                       |
| float                      | 56.8 ms                                                     | 45.6 ms: 1.25x faster                                                      |
| scimark_fft                | 184 ms                                                      | 151 ms: 1.22x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.14 ms: 1.19x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 41.1 ms: 1.18x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.16x faster                                                      |
| pyflate                    | 295 ms                                                      | 264 ms: 1.12x faster                                                       |
| fannkuch                   | 247 ms                                                      | 222 ms: 1.11x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.6 ms: 1.10x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 776 us: 1.10x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 180 us: 1.08x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 75.6 ms: 1.06x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 84.3 ms: 1.06x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.29 sec: 1.06x faster                                                     |
| chaos                      | 43.3 ms                                                     | 40.9 ms: 1.06x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.99 us: 1.05x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 490 ms: 1.05x faster                                                       |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.00 sec: 1.04x faster                                                     |
| logging_format             | 6.72 us                                                     | 6.44 us: 1.04x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 58.1 ns: 1.04x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 53.8 ms: 1.04x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                      |
| raytrace                   | 192 ms                                                      | 186 ms: 1.03x faster                                                       |
| json                       | 3.05 ms                                                     | 2.96 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 74.1 ms: 1.01x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 70.2 ms: 1.01x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 93.1 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.6 ms: 1.02x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 823 us: 1.02x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 90.1 ms: 1.03x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.05 ms: 1.03x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.89 ms: 1.03x slower                                                      |
| sympy_str                  | 175 ms                                                      | 182 ms: 1.04x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.2 ms: 1.04x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 97.6 ms: 1.05x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                     |
| unpickle_pure_python       | 133 us                                                      | 142 us: 1.06x slower                                                       |
| generators                 | 22.5 ms                                                     | 24.0 ms: 1.07x slower                                                      |
| go                         | 91.6 ms                                                     | 97.8 ms: 1.07x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                                     |
| sqlglot_normalize          | 187 ms                                                      | 200 ms: 1.07x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 37.0 ms: 1.07x slower                                                      |
| 2to3                       | 218 ms                                                      | 237 ms: 1.09x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 14.1 ms: 1.09x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.52 ms: 1.09x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.37 ms: 1.10x slower                                                      |
| sympy_expand               | 284 ms                                                      | 316 ms: 1.11x slower                                                       |
| async_generators           | 239 ms                                                      | 271 ms: 1.13x slower                                                       |
| coverage                   | 40.8 ms                                                     | 46.4 ms: 1.14x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.6 ms: 1.14x slower                                                      |
| richards_super             | 32.1 ms                                                     | 36.9 ms: 1.15x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.5 ms: 1.15x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.7 ms: 1.15x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.80 ms: 1.17x slower                                                      |
| django_template            | 22.9 ms                                                     | 26.9 ms: 1.17x slower                                                      |
| pycparser                  | 699 ms                                                      | 820 ms: 1.17x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 94.3 ms: 1.20x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 907 us: 1.21x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 118 us: 1.24x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 75.0 ms: 1.27x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 20.1 ms: 1.41x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (2): asyncio_tcp, nqueens
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 89.56% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown