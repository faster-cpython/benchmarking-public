# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-x86_64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.00x faster
- HPT reliability: 70.62%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 306 ms: 1.07x slower                                                       |
| docutils       | 2.87 sec                                                     | 3.12 sec: 1.09x slower                                                     |
| tornado_http   | 121 ms                                                       | 123 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.06x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 427 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 431 ms                                                       | 344 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 578 ms: 1.21x faster                                                       |
| async_tree_none            | 452 ms                                                       | 375 ms: 1.21x faster                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 877 ms: 1.20x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 470 ms: 1.16x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 906 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 618 ms: 1.13x faster                                                       |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                       |
| nbody          | 88.0 ms                                                      | 83.5 ms: 1.05x faster                                                      |
| float          | 76.6 ms                                                      | 74.8 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                        | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                       |
| regex_effbot   | 3.57 ms                                                      | 3.45 ms: 1.04x faster                                                      |
| regex_dna      | 239 ms                                                       | 238 ms: 1.00x faster                                                       |
| regex_v8       | 23.6 ms                                                      | 25.9 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                        | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 80.8 ms: 1.07x faster                                                      |
| pickle_dict          | 32.5 us                                                      | 31.4 us: 1.04x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 99.6 ms: 1.03x faster                                                      |
| tomli_loads          | 2.16 sec                                                     | 2.11 sec: 1.03x faster                                                     |
| pickle_pure_python   | 318 us                                                       | 312 us: 1.02x faster                                                       |
| pickle_list          | 4.43 us                                                      | 4.35 us: 1.02x faster                                                      |
| xml_etree_process    | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                                      |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.00x slower                                                       |
| pickle               | 10.5 us                                                      | 10.6 us: 1.01x slower                                                      |
| unpickle             | 14.8 us                                                      | 15.1 us: 1.02x slower                                                      |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.03x slower                                                      |
| unpickle_list        | 4.66 us                                                      | 4.85 us: 1.04x slower                                                      |
| unpickle_pure_python | 210 us                                                       | 220 us: 1.05x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.94 ms: 1.04x slower                                                      |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.24 ms: 1.08x faster                                                      |
| django_template | 38.2 ms                                                      | 41.5 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 427 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 431 ms                                                       | 344 ms: 1.25x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 29.6 us: 1.24x faster                                                      |
| deepcopy                   | 368 us                                                       | 304 us: 1.21x faster                                                       |
| comprehensions             | 21.9 us                                                      | 18.2 us: 1.21x faster                                                      |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 578 ms: 1.21x faster                                                       |
| async_tree_none            | 452 ms                                                       | 375 ms: 1.21x faster                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 877 ms: 1.20x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.3 ms: 1.16x faster                                                      |
| async_tree_memoization     | 544 ms                                                       | 470 ms: 1.16x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 906 ms: 1.15x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 70.4 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 618 ms: 1.13x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 82.9 ms: 1.11x faster                                                      |
| deepcopy_reduce            | 3.37 us                                                      | 3.05 us: 1.10x faster                                                      |
| mako                       | 10.0 ms                                                      | 9.24 ms: 1.08x faster                                                      |
| generators                 | 37.4 ms                                                      | 34.9 ms: 1.07x faster                                                      |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 3.92 ms: 1.07x faster                                                      |
| xml_etree_generate         | 86.1 ms                                                      | 80.8 ms: 1.07x faster                                                      |
| logging_format             | 7.48 us                                                      | 7.02 us: 1.07x faster                                                      |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                       |
| nbody                      | 88.0 ms                                                      | 83.5 ms: 1.05x faster                                                      |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.8 ms: 1.05x faster                                                      |
| logging_simple             | 6.71 us                                                      | 6.41 us: 1.05x faster                                                      |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                       |
| pickle_dict                | 32.5 us                                                      | 31.4 us: 1.04x faster                                                      |
| fannkuch                   | 350 ms                                                       | 337 ms: 1.04x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.45 ms: 1.04x faster                                                      |
| pprint_safe_repr           | 807 ms                                                       | 781 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 99.6 ms: 1.03x faster                                                      |
| scimark_fft                | 301 ms                                                       | 293 ms: 1.03x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 925 us: 1.03x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.11 sec: 1.03x faster                                                     |
| float                      | 76.6 ms                                                      | 74.8 ms: 1.02x faster                                                      |
| raytrace                   | 298 ms                                                       | 291 ms: 1.02x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                     |
| pickle_pure_python         | 318 us                                                       | 312 us: 1.02x faster                                                       |
| pickle_list                | 4.43 us                                                      | 4.35 us: 1.02x faster                                                      |
| async_generators           | 390 ms                                                       | 385 ms: 1.01x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.8 ms: 1.01x faster                                                      |
| xml_etree_process          | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                                      |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                     |
| regex_dna                  | 239 ms                                                       | 238 ms: 1.00x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.00x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 380 ms: 1.00x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.79 us: 1.01x slower                                                      |
| pyflate                    | 439 ms                                                       | 442 ms: 1.01x slower                                                       |
| pickle                     | 10.5 us                                                      | 10.6 us: 1.01x slower                                                      |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                     |
| asyncio_websockets         | 387 ms                                                       | 392 ms: 1.01x slower                                                       |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.02x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.1 us: 1.02x slower                                                      |
| tornado_http               | 121 ms                                                       | 123 ms: 1.02x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 67.1 ms: 1.03x slower                                                      |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.03x slower                                                      |
| sqlglot_transpile          | 1.78 ms                                                      | 1.84 ms: 1.03x slower                                                      |
| dask                       | 392 ms                                                       | 405 ms: 1.03x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.94 ms: 1.04x slower                                                      |
| sympy_sum                  | 162 ms                                                       | 168 ms: 1.04x slower                                                       |
| chaos                      | 64.0 ms                                                      | 66.3 ms: 1.04x slower                                                      |
| sympy_str                  | 302 ms                                                       | 314 ms: 1.04x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 93.3 ms: 1.04x slower                                                      |
| unpickle_list              | 4.66 us                                                      | 4.85 us: 1.04x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.44 ms: 1.04x slower                                                      |
| richards_super             | 51.3 ms                                                      | 53.7 ms: 1.05x slower                                                      |
| unpickle_pure_python       | 210 us                                                       | 220 us: 1.05x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                      |
| json                       | 5.12 ms                                                      | 5.41 ms: 1.06x slower                                                      |
| 2to3                       | 285 ms                                                       | 306 ms: 1.07x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 25.7 ms: 1.07x slower                                                      |
| django_template            | 38.2 ms                                                      | 41.5 ms: 1.09x slower                                                      |
| sqlglot_optimize           | 57.5 ms                                                      | 62.5 ms: 1.09x slower                                                      |
| docutils                   | 2.87 sec                                                     | 3.12 sec: 1.09x slower                                                     |
| sympy_expand               | 484 ms                                                       | 529 ms: 1.09x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.9 ms: 1.09x slower                                                      |
| sqlglot_normalize          | 116 ms                                                       | 128 ms: 1.11x slower                                                       |
| go                         | 150 ms                                                       | 166 ms: 1.11x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 105 ns: 1.11x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.66 ms: 1.12x slower                                                      |
| deltablue                  | 3.24 ms                                                      | 3.69 ms: 1.14x slower                                                      |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                      |
| telco                      | 6.96 ms                                                      | 8.17 ms: 1.17x slower                                                      |
| scimark_lu                 | 98.8 ms                                                      | 116 ms: 1.18x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.92 ms: 1.20x slower                                                      |
| typing_runtime_protocols   | 152 us                                                       | 185 us: 1.22x slower                                                       |
| scimark_sor                | 109 ms                                                       | 136 ms: 1.25x slower                                                       |
| coverage                   | 66.7 ms                                                      | 83.4 ms: 1.25x slower                                                      |
| gc_traversal               | 3.48 ms                                                      | 4.42 ms: 1.27x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                               |

Benchmark hidden because not significant (3): mdp, richards, bench_mp_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240618-3.14.0a0-a1bdb94-JIT/bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 70.62% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x