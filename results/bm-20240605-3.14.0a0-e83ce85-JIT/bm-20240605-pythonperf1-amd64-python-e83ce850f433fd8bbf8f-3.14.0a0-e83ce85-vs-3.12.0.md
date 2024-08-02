# Results vs. 3.12.0

- fork: python
- ref: e83ce850f433fd8bbf8f
- machine: windows-amd64
- commit hash: e83ce85
- commit date: 2024-06-05
- overall geometric mean: 1.05x faster
- HPT reliability: 99.23%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 230 ms: 1.05x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.78 sec: 1.07x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 86.2 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 266 ms: 1.38x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 210 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 387 ms: 1.30x faster                                                       |
| async_tree_none            | 291 ms                                                      | 229 ms: 1.27x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 617 ms: 1.25x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 277 ms: 1.22x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 400 ms: 1.22x faster                                                       |
| async_tree_io              | 731 ms                                                      | 603 ms: 1.21x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.28x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 53.1 ms: 1.35x faster                                                      |
| float          | 56.8 ms                                                     | 44.2 ms: 1.29x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 88.3 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 172 us: 1.13x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 51.2 ms: 1.09x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 129 us: 1.03x faster                                                       |
| pickle_list          | 2.83 us                                                     | 2.73 us: 1.03x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 17.8 us: 1.03x faster                                                      |
| pickle               | 7.43 us                                                     | 7.29 us: 1.02x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 91.5 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.3 ms: 1.01x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.75 ms: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.82 us: 1.02x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.77 us: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.8 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.24 ms: 1.35x faster                                                      |
| django_template | 22.9 ms                                                     | 25.2 ms: 1.10x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| spectral_norm              | 66.9 ms                                                     | 44.2 ms: 1.51x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.41 sec: 1.48x faster                                                     |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.38x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 266 ms: 1.38x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 210 ms: 1.36x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.24 ms: 1.35x faster                                                      |
| nbody                      | 71.9 ms                                                     | 53.1 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 387 ms: 1.30x faster                                                       |
| float                      | 56.8 ms                                                     | 44.2 ms: 1.29x faster                                                      |
| async_tree_none            | 291 ms                                                      | 229 ms: 1.27x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 617 ms: 1.25x faster                                                       |
| scimark_fft                | 184 ms                                                      | 150 ms: 1.23x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 277 ms: 1.22x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 400 ms: 1.22x faster                                                       |
| async_tree_io              | 731 ms                                                      | 603 ms: 1.21x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.14 ms: 1.20x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 41.6 ms: 1.17x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.7 ms: 1.16x faster                                                      |
| pyflate                    | 295 ms                                                      | 257 ms: 1.15x faster                                                       |
| fannkuch                   | 247 ms                                                      | 217 ms: 1.13x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 172 us: 1.13x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.9 us: 1.13x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                     |
| pprint_safe_repr           | 513 ms                                                      | 457 ms: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 949 ms: 1.10x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 51.2 ms: 1.09x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 55.4 ns: 1.09x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.1 ms: 1.09x faster                                                      |
| raytrace                   | 192 ms                                                      | 178 ms: 1.08x faster                                                       |
| chaos                      | 43.3 ms                                                     | 40.1 ms: 1.08x faster                                                      |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.84 us: 1.07x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 74.9 ms: 1.07x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.27 us: 1.07x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 809 us: 1.06x faster                                                       |
| json                       | 3.05 ms                                                     | 2.90 ms: 1.05x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.6 ms: 1.04x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 86.2 ms: 1.04x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 470 ms: 1.04x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.5 ms: 1.04x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 129 us: 1.03x faster                                                       |
| pickle_list                | 2.83 us                                                     | 2.73 us: 1.03x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 17.8 us: 1.03x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.29 us: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 73.3 ms: 1.02x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 91.5 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.3 ms: 1.01x faster                                                      |
| sqlglot_parse              | 804 us                                                      | 808 us: 1.00x slower                                                       |
| deepcopy                   | 238 us                                                      | 239 us: 1.01x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.75 ms: 1.01x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 88.3 ms: 1.01x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.04 ms: 1.01x slower                                                      |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.82 us: 1.02x slower                                                      |
| go                         | 91.6 ms                                                     | 93.8 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 94.3 ms: 1.03x slower                                                      |
| 2to3                       | 218 ms                                                      | 230 ms: 1.05x slower                                                       |
| richards_super             | 32.1 ms                                                     | 33.8 ms: 1.05x slower                                                      |
| async_generators           | 239 ms                                                      | 254 ms: 1.06x slower                                                       |
| richards                   | 28.4 ms                                                     | 30.1 ms: 1.06x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.78 sec: 1.07x slower                                                     |
| unpickle                   | 8.18 us                                                     | 8.77 us: 1.07x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 84.7 ms: 1.07x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 37.3 ms: 1.08x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.49 sec: 1.08x slower                                                     |
| sympy_integrate            | 13.0 ms                                                     | 14.0 ms: 1.08x slower                                                      |
| sympy_expand               | 284 ms                                                      | 309 ms: 1.09x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.35 ms: 1.09x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.2 ms: 1.10x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.55 ms: 1.10x slower                                                      |
| python_startup             | 19.5 ms                                                     | 21.8 ms: 1.12x slower                                                      |
| coverage                   | 40.8 ms                                                     | 45.8 ms: 1.12x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.67 ms: 1.14x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 69.1 ms: 1.17x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 908 us: 1.21x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (4): bench_mp_pool, deepcopy_reduce, regex_v8, pycparser
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (5) of results/bm-20240605-3.14.0a0-e83ce85-JIT/bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.23% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown