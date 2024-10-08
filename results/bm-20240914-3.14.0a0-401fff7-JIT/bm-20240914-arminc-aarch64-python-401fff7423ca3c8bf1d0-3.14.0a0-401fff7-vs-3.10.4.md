# Results vs. 3.10.4

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-aarch64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 3.98 sec: 1.13x slower                                                  |
| html5lib       | 86.5 ms                                                               | 71.3 ms: 1.21x faster                                                   |
| tornado_http   | 178 ms                                                                | 147 ms: 1.21x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 444 ms: 2.14x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.14 sec: 2.00x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 588 ms: 1.93x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 757 ms: 1.68x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.93x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.5 ms: 1.54x faster                                                   |
| nbody          | 166 ms                                                                | 114 ms: 1.46x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 242 ms: 1.06x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 31.5 ms: 1.02x faster                                                   |
| regex_compile  | 177 ms                                                                | 190 ms: 1.08x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 380 us: 1.39x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 267 us: 1.37x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.9 ms: 1.25x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 188 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.41 us: 1.09x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.04x faster                                                    |
| json_loads           | 30.9 us                                                               | 31.5 us: 1.02x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.2 us: 1.09x slower                                                   |
| pickle               | 12.5 us                                                               | 13.8 us: 1.10x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.4 us: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                            |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.80 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.1 ms: 1.45x faster                                                   |
| django_template | 53.3 ms                                                               | 50.8 ms: 1.05x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 35.7 ms: 1.01x slower                                                   |
| genshi_xml      | 69.8 ms                                                               | 82.2 ms: 1.18x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.06x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.19x faster                                                    |
| async_tree_none          | 950 ms                                                                | 444 ms: 2.14x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.36 ms: 2.05x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.14 sec: 2.00x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 588 ms: 1.93x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.57 ms: 1.92x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 757 ms: 1.68x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.2 us: 1.66x faster                                                   |
| raytrace                 | 573 ms                                                                | 350 ms: 1.64x faster                                                    |
| scimark_sor              | 246 ms                                                                | 152 ms: 1.62x faster                                                    |
| logging_silent           | 222 ns                                                                | 140 ns: 1.59x faster                                                    |
| float                    | 135 ms                                                                | 87.5 ms: 1.54x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 619 ms: 1.53x faster                                                    |
| scimark_lu               | 227 ms                                                                | 149 ms: 1.52x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 89.4 ms: 1.50x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.25 sec: 1.46x faster                                                  |
| nbody                    | 166 ms                                                                | 114 ms: 1.46x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.1 ms: 1.45x faster                                                   |
| richards_super           | 107 ms                                                                | 75.3 ms: 1.42x faster                                                   |
| go                       | 264 ms                                                                | 186 ms: 1.42x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 380 us: 1.39x faster                                                    |
| richards                 | 91.7 ms                                                               | 66.3 ms: 1.38x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 92.5 ms: 1.38x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 267 us: 1.37x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.77 ms: 1.36x faster                                                   |
| comprehensions           | 33.1 us                                                               | 24.5 us: 1.35x faster                                                   |
| chaos                    | 121 ms                                                                | 92.1 ms: 1.31x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.6 ms: 1.30x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.52 us: 1.30x faster                                                   |
| deepcopy                 | 511 us                                                                | 394 us: 1.30x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.20 us: 1.29x faster                                                   |
| spectral_norm            | 186 ms                                                                | 145 ms: 1.28x faster                                                    |
| thrift                   | 1.26 ms                                                               | 981 us: 1.28x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.21 ms: 1.28x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| xml_etree_process        | 99.5 ms                                                               | 79.9 ms: 1.25x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.5 ms: 1.22x faster                                                   |
| pyflate                  | 795 ms                                                                | 654 ms: 1.22x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 71.3 ms: 1.21x faster                                                   |
| tornado_http             | 178 ms                                                                | 147 ms: 1.21x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.86 us: 1.19x faster                                                   |
| generators               | 68.1 ms                                                               | 57.4 ms: 1.19x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.36 ms: 1.17x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 188 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.82 ms: 1.12x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.54 sec: 1.10x faster                                                  |
| scimark_fft              | 500 ms                                                                | 459 ms: 1.09x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.41 us: 1.09x faster                                                   |
| fannkuch                 | 546 ms                                                                | 503 ms: 1.08x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 10.2 ms: 1.07x faster                                                   |
| regex_dna                | 257 ms                                                                | 242 ms: 1.06x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.88 us: 1.06x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.50 sec: 1.06x faster                                                  |
| django_template          | 53.3 ms                                                               | 50.8 ms: 1.05x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.04x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 151 ms: 1.03x faster                                                    |
| json                     | 5.88 ms                                                               | 5.73 ms: 1.03x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 31.5 ms: 1.02x faster                                                   |
| meteor_contest           | 126 ms                                                                | 124 ms: 1.02x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 663 ms: 1.01x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 35.7 ms: 1.01x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.29 ms: 1.01x slower                                                   |
| json_loads               | 30.9 us                                                               | 31.5 us: 1.02x slower                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 78.9 ms: 1.05x slower                                                   |
| regex_compile            | 177 ms                                                                | 190 ms: 1.08x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 38.2 us: 1.09x slower                                                   |
| sympy_integrate          | 26.5 ms                                                               | 29.0 ms: 1.09x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.25 sec: 1.09x slower                                                  |
| nqueens                  | 117 ms                                                                | 128 ms: 1.09x slower                                                    |
| dulwich_log              | 73.5 ms                                                               | 80.8 ms: 1.10x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.8 us: 1.10x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.60 sec: 1.10x slower                                                  |
| async_generators         | 452 ms                                                                | 501 ms: 1.11x slower                                                    |
| unpickle                 | 17.5 us                                                               | 19.4 us: 1.11x slower                                                   |
| sympy_str                | 329 ms                                                                | 368 ms: 1.12x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.98 sec: 1.13x slower                                                  |
| sympy_expand             | 543 ms                                                                | 618 ms: 1.14x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| sympy_sum                | 184 ms                                                                | 216 ms: 1.17x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 82.2 ms: 1.18x slower                                                   |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.20x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.10 ms: 1.23x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.5 ms: 1.23x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.80 ms: 1.28x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.18x faster                                                            |

Benchmark hidden because not significant (4): pylint, pickle_list, pidigits, 2to3
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.24x