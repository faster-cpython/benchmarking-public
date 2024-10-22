# Results vs. 3.10.4

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-aarch64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.18x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 3.94 sec: 1.12x slower                                                  |
| html5lib       | 86.5 ms                                                               | 71.9 ms: 1.20x faster                                                   |
| tornado_http   | 178 ms                                                                | 150 ms: 1.19x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 442 ms: 2.15x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 589 ms: 1.93x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 748 ms: 1.70x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.93x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.5 ms: 1.54x faster                                                   |
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                                   |
| regex_dna      | 257 ms                                                                | 252 ms: 1.02x faster                                                    |
| regex_compile  | 177 ms                                                                | 196 ms: 1.11x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 267 us: 1.37x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 392 us: 1.35x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 187 ms: 1.14x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.42 us: 1.09x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| pickle_list          | 5.24 us                                                               | 5.20 us: 1.01x faster                                                   |
| json_loads           | 30.9 us                                                               | 31.4 us: 1.02x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.3 us: 1.09x slower                                                   |
| pickle               | 12.5 us                                                               | 13.7 us: 1.10x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.3 us: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.79 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.9 ms: 1.47x faster                                                   |
| django_template | 53.3 ms                                                               | 51.4 ms: 1.04x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 35.0 ms: 1.01x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 80.8 ms: 1.16x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 213 us: 3.10x faster                                                    |
| async_tree_none          | 950 ms                                                                | 442 ms: 2.15x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.39 ms: 2.04x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 589 ms: 1.93x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.57 ms: 1.92x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 748 ms: 1.70x faster                                                    |
| raytrace                 | 573 ms                                                                | 348 ms: 1.65x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.6 us: 1.64x faster                                                   |
| logging_silent           | 222 ns                                                                | 137 ns: 1.62x faster                                                    |
| scimark_sor              | 246 ms                                                                | 152 ms: 1.61x faster                                                    |
| float                    | 135 ms                                                                | 87.5 ms: 1.54x faster                                                   |
| scimark_lu               | 227 ms                                                                | 148 ms: 1.53x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 629 ms: 1.50x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 89.7 ms: 1.49x faster                                                   |
| mako                     | 18.9 ms                                                               | 12.9 ms: 1.47x faster                                                   |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.27 sec: 1.45x faster                                                  |
| richards_super           | 107 ms                                                                | 75.9 ms: 1.41x faster                                                   |
| go                       | 264 ms                                                                | 190 ms: 1.39x faster                                                    |
| richards                 | 91.7 ms                                                               | 66.3 ms: 1.38x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 92.6 ms: 1.38x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 267 us: 1.37x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.76 ms: 1.37x faster                                                   |
| comprehensions           | 33.1 us                                                               | 24.5 us: 1.35x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 392 us: 1.35x faster                                                    |
| chaos                    | 121 ms                                                                | 92.2 ms: 1.31x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.46 us: 1.31x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.5 ms: 1.30x faster                                                   |
| thrift                   | 1.26 ms                                                               | 970 us: 1.30x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.20 us: 1.29x faster                                                   |
| spectral_norm            | 186 ms                                                                | 146 ms: 1.28x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.23 ms: 1.27x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| deepcopy                 | 511 us                                                                | 401 us: 1.27x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.7 ms: 1.21x faster                                                   |
| pyflate                  | 795 ms                                                                | 657 ms: 1.21x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 71.9 ms: 1.20x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.83 us: 1.20x faster                                                   |
| tornado_http             | 178 ms                                                                | 150 ms: 1.19x faster                                                    |
| generators               | 68.1 ms                                                               | 57.6 ms: 1.18x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 187 ms: 1.14x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.85 ms: 1.11x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.53 sec: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                                    |
| scimark_fft              | 500 ms                                                                | 459 ms: 1.09x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.42 us: 1.09x faster                                                   |
| fannkuch                 | 546 ms                                                                | 508 ms: 1.07x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.84 us: 1.07x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 10.3 ms: 1.05x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.52 sec: 1.05x faster                                                  |
| sqlglot_normalize        | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| django_template          | 53.3 ms                                                               | 51.4 ms: 1.04x faster                                                   |
| json                     | 5.88 ms                                                               | 5.67 ms: 1.04x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                                   |
| regex_dna                | 257 ms                                                                | 252 ms: 1.02x faster                                                    |
| meteor_contest           | 126 ms                                                                | 124 ms: 1.02x faster                                                    |
| pickle_list              | 5.24 us                                                               | 5.20 us: 1.01x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 35.0 ms: 1.01x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 663 ms: 1.01x slower                                                    |
| json_loads               | 30.9 us                                                               | 31.4 us: 1.02x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.31 ms: 1.02x slower                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 78.5 ms: 1.04x slower                                                   |
| nqueens                  | 117 ms                                                                | 126 ms: 1.07x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 28.5 ms: 1.07x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.25 sec: 1.09x slower                                                  |
| pickle_dict              | 35.1 us                                                               | 38.3 us: 1.09x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.7 us: 1.10x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.3 us: 1.10x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.61 sec: 1.11x slower                                                  |
| regex_compile            | 177 ms                                                                | 196 ms: 1.11x slower                                                    |
| dulwich_log              | 73.5 ms                                                               | 82.0 ms: 1.12x slower                                                   |
| docutils                 | 3.53 sec                                                              | 3.94 sec: 1.12x slower                                                  |
| sympy_str                | 329 ms                                                                | 369 ms: 1.12x slower                                                    |
| sympy_expand             | 543 ms                                                                | 613 ms: 1.13x slower                                                    |
| async_generators         | 452 ms                                                                | 512 ms: 1.13x slower                                                    |
| sympy_sum                | 184 ms                                                                | 211 ms: 1.15x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 80.8 ms: 1.16x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.10 ms: 1.23x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.6 ms: 1.25x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.79 ms: 1.28x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.18x faster                                                            |

Benchmark hidden because not significant (3): pylint, pidigits, 2to3
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.25x