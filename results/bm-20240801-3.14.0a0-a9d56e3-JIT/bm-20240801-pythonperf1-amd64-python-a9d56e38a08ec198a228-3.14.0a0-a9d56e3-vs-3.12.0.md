# Results vs. 3.12.0

- fork: python
- ref: a9d56e38a08ec198a228
- machine: windows-amd64
- commit hash: a9d56e3
- commit date: 2024-08-01
- overall geometric mean: 1.05x faster
- HPT reliability: 84.32%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 240 ms: 1.10x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.85 sec: 1.11x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 95.5 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 194 ms: 1.47x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 250 ms: 1.47x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 537 ms: 1.44x faster                                                       |
| async_tree_none            | 291 ms                                                      | 212 ms: 1.38x faster                                                       |
| async_tree_io              | 731 ms                                                      | 545 ms: 1.34x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 379 ms: 1.32x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 261 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 393 ms: 1.24x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.37x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 51.5 ms: 1.40x faster                                                      |
| float          | 56.8 ms                                                     | 45.4 ms: 1.25x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 91.7 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.26 sec: 1.08x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 52.3 ms: 1.07x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 184 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.2 ms: 1.05x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 137 us: 1.03x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 5.99 ms: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 4.97 ms: 1.43x faster                                                      |
| django_template | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.42 sec: 1.48x faster                                                     |
| async_tree_none_tg         | 285 ms                                                      | 194 ms: 1.47x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 16.1 us: 1.47x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 250 ms: 1.47x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 45.8 ms: 1.46x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 537 ms: 1.44x faster                                                       |
| mako                       | 7.09 ms                                                     | 4.97 ms: 1.43x faster                                                      |
| nbody                      | 71.9 ms                                                     | 51.5 ms: 1.40x faster                                                      |
| async_tree_none            | 291 ms                                                      | 212 ms: 1.38x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.38x faster                                                      |
| async_tree_io              | 731 ms                                                      | 545 ms: 1.34x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 379 ms: 1.32x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 261 ms: 1.30x faster                                                       |
| deepcopy                   | 238 us                                                      | 185 us: 1.29x faster                                                       |
| scimark_fft                | 184 ms                                                      | 147 ms: 1.25x faster                                                       |
| float                      | 56.8 ms                                                     | 45.4 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 393 ms: 1.24x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.07 ms: 1.24x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 39.4 ms: 1.23x faster                                                      |
| pyflate                    | 295 ms                                                      | 247 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.82 us: 1.15x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.0 ms: 1.15x faster                                                      |
| fannkuch                   | 247 ms                                                      | 215 ms: 1.15x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.4 ms: 1.10x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.26 sec: 1.08x faster                                                     |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 52.3 ms: 1.07x faster                                                      |
| pickle_pure_python         | 195 us                                                      | 184 us: 1.06x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 484 ms: 1.06x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 70.7 ms: 1.06x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 814 us: 1.05x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 995 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.2 ms: 1.05x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.06 us: 1.04x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 58.7 ns: 1.03x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.53 us: 1.03x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 43.1 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 62.3 ms: 1.01x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 81.0 ms: 1.01x slower                                                      |
| generators                 | 22.5 ms                                                     | 23.0 ms: 1.02x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 192 ms: 1.03x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 137 us: 1.03x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.58 ms: 1.03x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 91.7 ms: 1.05x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 844 us: 1.05x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.99 ms: 1.05x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 96.3 ms: 1.05x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.08 ms: 1.06x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 73.0 ms: 1.06x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                     |
| sqlglot_optimize           | 34.5 ms                                                     | 36.8 ms: 1.07x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 95.5 ms: 1.07x slower                                                      |
| sympy_str                  | 175 ms                                                      | 189 ms: 1.08x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.35 ms: 1.09x slower                                                      |
| async_generators           | 239 ms                                                      | 261 ms: 1.09x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                      |
| go                         | 91.6 ms                                                     | 101 ms: 1.10x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.54 ms: 1.10x slower                                                      |
| 2to3                       | 218 ms                                                      | 240 ms: 1.10x slower                                                       |
| richards_super             | 32.1 ms                                                     | 35.6 ms: 1.11x slower                                                      |
| richards                   | 28.4 ms                                                     | 31.5 ms: 1.11x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.85 sec: 1.11x slower                                                     |
| pycparser                  | 699 ms                                                      | 786 ms: 1.12x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                      |
| python_startup             | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.7 ms: 1.13x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 555 ms: 1.14x slower                                                       |
| sympy_expand               | 284 ms                                                      | 330 ms: 1.16x slower                                                       |
| coverage                   | 40.8 ms                                                     | 47.7 ms: 1.17x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 92.7 ms: 1.18x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.83 ms: 1.18x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 912 us: 1.21x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 118 us: 1.24x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 75.2 ms: 1.28x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (4): xml_etree_parse, raytrace, xml_etree_process, json
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240801-3.14.0a0-a9d56e3-JIT/bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 84.32% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown