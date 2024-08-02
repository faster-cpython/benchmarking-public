# Results vs. 3.12.0

- fork: python
- ref: 68e279b37aae3019979a
- machine: windows-amd64
- commit hash: 68e279b
- commit date: 2024-07-07
- overall geometric mean: 1.07x faster
- HPT reliability: 99.61%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 230 ms: 1.06x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 84.4 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 186 ms: 1.53x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 242 ms: 1.51x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 516 ms: 1.49x faster                                                       |
| async_tree_none            | 291 ms                                                      | 206 ms: 1.42x faster                                                       |
| async_tree_io              | 731 ms                                                      | 519 ms: 1.41x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 252 ms: 1.35x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 382 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 382 ms: 1.28x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.41x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 52.2 ms: 1.38x faster                                                      |
| float          | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 19.9 ms: 1.40x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 174 us: 1.12x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 51.8 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 127 us: 1.05x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 37.1 ms: 1.02x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 92.1 ms: 1.01x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.1 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.10 ms: 1.39x faster                                                      |
| django_template | 22.9 ms                                                     | 27.1 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.36 sec: 1.54x faster                                                     |
| async_tree_none_tg         | 285 ms                                                      | 186 ms: 1.53x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 242 ms: 1.51x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 15.7 us: 1.51x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 516 ms: 1.49x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 45.7 ms: 1.47x faster                                                      |
| async_tree_none            | 291 ms                                                      | 206 ms: 1.42x faster                                                       |
| async_tree_io              | 731 ms                                                      | 519 ms: 1.41x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.10 ms: 1.39x faster                                                      |
| nbody                      | 71.9 ms                                                     | 52.2 ms: 1.38x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.37x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 252 ms: 1.35x faster                                                       |
| deepcopy                   | 238 us                                                      | 180 us: 1.32x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 382 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 382 ms: 1.28x faster                                                       |
| float                      | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                                      |
| scimark_fft                | 184 ms                                                      | 149 ms: 1.24x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.15 ms: 1.19x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 41.1 ms: 1.18x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.9 ms: 1.15x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.83 us: 1.15x faster                                                      |
| pyflate                    | 295 ms                                                      | 258 ms: 1.14x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 174 us: 1.12x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 769 us: 1.11x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 466 ms: 1.10x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 952 ms: 1.10x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                     |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| chaos                      | 43.3 ms                                                     | 40.1 ms: 1.08x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 51.8 ms: 1.08x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.84 us: 1.07x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 56.3 ns: 1.07x faster                                                      |
| fannkuch                   | 247 ms                                                      | 230 ms: 1.07x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.28 us: 1.07x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 84.4 ms: 1.06x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 76.0 ms: 1.06x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 127 us: 1.05x faster                                                       |
| raytrace                   | 192 ms                                                      | 184 ms: 1.05x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.6 ms: 1.05x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| json                       | 3.05 ms                                                     | 2.96 ms: 1.03x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 61.7 ms: 1.02x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 37.1 ms: 1.02x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 92.1 ms: 1.01x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 68.7 ms: 1.01x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 92.2 ms: 1.01x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.03 ms: 1.01x slower                                                      |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                       |
| generators                 | 22.5 ms                                                     | 22.8 ms: 1.01x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 35.1 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                      |
| go                         | 91.6 ms                                                     | 93.6 ms: 1.02x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| richards                   | 28.4 ms                                                     | 29.3 ms: 1.03x slower                                                      |
| richards_super             | 32.1 ms                                                     | 33.2 ms: 1.04x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.25 ms: 1.04x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                     |
| 2to3                       | 218 ms                                                      | 230 ms: 1.06x slower                                                       |
| async_generators           | 239 ms                                                      | 253 ms: 1.06x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.9 ms: 1.07x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                      |
| sympy_expand               | 284 ms                                                      | 305 ms: 1.08x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.48 ms: 1.08x slower                                                      |
| python_startup             | 19.5 ms                                                     | 21.1 ms: 1.09x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.09x slower                                                     |
| scimark_sor                | 78.8 ms                                                     | 87.9 ms: 1.12x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.64 ms: 1.13x slower                                                      |
| pycparser                  | 699 ms                                                      | 792 ms: 1.13x slower                                                       |
| coverage                   | 40.8 ms                                                     | 46.4 ms: 1.14x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 68.5 ms: 1.16x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                       |
| django_template            | 22.9 ms                                                     | 27.1 ms: 1.18x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 902 us: 1.20x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 19.9 ms: 1.40x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (6): asyncio_tcp, sqlglot_normalize, json_dumps, sqlglot_parse, meteor_contest, regex_compile
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240707-3.14.0a0-68e279b-JIT/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.61% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown