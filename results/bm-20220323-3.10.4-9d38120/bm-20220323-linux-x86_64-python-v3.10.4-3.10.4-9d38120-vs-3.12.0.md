
# Results vs. 3.12.0

- fork: python
- ref: v3.10.4
- machine: linux-x86_64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.30x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x slower
- Memory change: 0.89x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 348 ms: 1.27x slower                                   |
| chameleon      | 7.41 ms                                                | 9.68 ms: 1.31x slower                                  |
| docutils       | 2.77 sec                                               | 3.30 sec: 1.19x slower                                 |
| tornado_http   | 103 ms                                                 | 136 ms: 1.33x slower                                   |
| Geometric mean | (ref)                                                  | 1.27x slower                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_cpu_io_mixed | 726 ms                                                 | 1.02 sec: 1.40x slower                                 |
| async_tree_memoization  | 578 ms                                                 | 870 ms: 1.51x slower                                   |
| async_tree_io           | 1.16 sec                                               | 1.77 sec: 1.53x slower                                 |
| async_tree_none         | 472 ms                                                 | 728 ms: 1.54x slower                                   |
| Geometric mean          | (ref)                                                  | 1.49x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                   |
| float          | 84.7 ms                                                | 117 ms: 1.38x slower                                   |
| nbody          | 97.0 ms                                                | 154 ms: 1.58x slower                                   |
| Geometric mean | (ref)                                                  | 1.31x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                   |
| regex_v8       | 23.1 ms                                                | 27.8 ms: 1.20x slower                                  |
| regex_compile  | 148 ms                                                 | 188 ms: 1.27x slower                                   |
| Geometric mean | (ref)                                                  | 1.13x slower                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_dict          | 35.5 us                                                | 29.6 us: 1.20x faster                                  |
| unpickle             | 15.9 us                                                | 14.4 us: 1.10x faster                                  |
| pickle               | 11.6 us                                                | 10.7 us: 1.09x faster                                  |
| unpickle_list        | 5.29 us                                                | 5.20 us: 1.02x faster                                  |
| xml_etree_parse      | 159 ms                                                 | 168 ms: 1.05x slower                                   |
| xml_etree_iterparse  | 107 ms                                                 | 115 ms: 1.08x slower                                   |
| json_loads           | 28.5 us                                                | 31.2 us: 1.09x slower                                  |
| xml_etree_generate   | 89.2 ms                                                | 99.4 ms: 1.12x slower                                  |
| xml_etree_process    | 61.7 ms                                                | 79.1 ms: 1.28x slower                                  |
| tomli_loads          | 2.33 sec                                               | 3.14 sec: 1.35x slower                                 |
| json_dumps           | 10.4 ms                                                | 14.2 ms: 1.36x slower                                  |
| unpickle_pure_python | 230 us                                                 | 331 us: 1.44x slower                                   |
| pickle_pure_python   | 324 us                                                 | 484 us: 1.50x slower                                   |
| Geometric mean       | (ref)                                                  | 1.12x slower                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 5.93 ms: 1.17x faster                                  |
| python_startup         | 9.55 ms                                                | 14.6 ms: 1.53x slower                                  |
| Geometric mean         | (ref)                                                  | 1.14x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 11.9 ms                                                | 16.3 ms: 1.37x slower                                  |
| django_template | 34.6 ms                                                | 48.2 ms: 1.39x slower                                  |
| Geometric mean  | (ref)                                                  | 1.38x slower                                           |

All benchmarks:
===============

| Benchmark                | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_dict              | 35.5 us                                                | 29.6 us: 1.20x faster                                  |
| python_startup_no_site   | 6.94 ms                                                | 5.93 ms: 1.17x faster                                  |
| unpickle                 | 15.9 us                                                | 14.4 us: 1.10x faster                                  |
| pickle                   | 11.6 us                                                | 10.7 us: 1.09x faster                                  |
| gc_traversal             | 3.79 ms                                                | 3.62 ms: 1.05x faster                                  |
| async_generators         | 463 ms                                                 | 444 ms: 1.04x faster                                   |
| unpickle_list            | 5.29 us                                                | 5.20 us: 1.02x faster                                  |
| asyncio_websockets       | 551 ms                                                 | 559 ms: 1.01x slower                                   |
| pidigits                 | 187 ms                                                 | 191 ms: 1.02x slower                                   |
| telco                    | 7.10 ms                                                | 7.27 ms: 1.02x slower                                  |
| xml_etree_parse          | 159 ms                                                 | 168 ms: 1.05x slower                                   |
| pathlib                  | 19.3 ms                                                | 20.5 ms: 1.06x slower                                  |
| meteor_contest           | 112 ms                                                 | 120 ms: 1.06x slower                                   |
| sqlite_synth             | 2.83 us                                                | 3.02 us: 1.07x slower                                  |
| regex_dna                | 212 ms                                                 | 227 ms: 1.07x slower                                   |
| mypy2                    | 830 ms                                                 | 894 ms: 1.08x slower                                   |
| xml_etree_iterparse      | 107 ms                                                 | 115 ms: 1.08x slower                                   |
| json                     | 5.26 ms                                                | 5.69 ms: 1.08x slower                                  |
| mdp                      | 2.63 sec                                               | 2.85 sec: 1.08x slower                                 |
| coverage                 | 72.7 ms                                                | 79.4 ms: 1.09x slower                                  |
| json_loads               | 28.5 us                                                | 31.2 us: 1.09x slower                                  |
| create_gc_cycles         | 1.48 ms                                                | 1.62 ms: 1.10x slower                                  |
| unpack_sequence          | 54.0 ns                                                | 60.0 ns: 1.11x slower                                  |
| xml_etree_generate       | 89.2 ms                                                | 99.4 ms: 1.12x slower                                  |
| sympy_str                | 300 ms                                                 | 346 ms: 1.15x slower                                   |
| sympy_sum                | 169 ms                                                 | 196 ms: 1.16x slower                                   |
| bench_thread_pool        | 842 us                                                 | 986 us: 1.17x slower                                   |
| sqlalchemy_declarative   | 147 ms                                                 | 172 ms: 1.17x slower                                   |
| sympy_expand             | 478 ms                                                 | 566 ms: 1.18x slower                                   |
| dask                     | 372 ms                                                 | 441 ms: 1.19x slower                                   |
| docutils                 | 2.77 sec                                               | 3.30 sec: 1.19x slower                                 |
| regex_v8                 | 23.1 ms                                                | 27.8 ms: 1.20x slower                                  |
| sympy_integrate          | 21.4 ms                                                | 25.8 ms: 1.20x slower                                  |
| scimark_fft              | 382 ms                                                 | 466 ms: 1.22x slower                                   |
| dulwich_log              | 68.5 ms                                                | 84.3 ms: 1.23x slower                                  |
| gunicorn                 | 1.24 ms                                                | 1.53 ms: 1.23x slower                                  |
| deepcopy_reduce          | 3.35 us                                                | 4.17 us: 1.25x slower                                  |
| sqlalchemy_imperative    | 18.7 ms                                                | 23.3 ms: 1.25x slower                                  |
| aiohttp                  | 1.15 ms                                                | 1.44 ms: 1.25x slower                                  |
| logging_format           | 7.23 us                                                | 9.09 us: 1.26x slower                                  |
| sqlglot_optimize         | 54.8 ms                                                | 69.2 ms: 1.26x slower                                  |
| regex_compile            | 148 ms                                                 | 188 ms: 1.27x slower                                   |
| nqueens                  | 83.3 ms                                                | 106 ms: 1.27x slower                                   |
| 2to3                     | 274 ms                                                 | 348 ms: 1.27x slower                                   |
| fannkuch                 | 417 ms                                                 | 532 ms: 1.27x slower                                   |
| scimark_sparse_mat_mult  | 5.06 ms                                                | 6.47 ms: 1.28x slower                                  |
| xml_etree_process        | 61.7 ms                                                | 79.1 ms: 1.28x slower                                  |
| logging_simple           | 6.46 us                                                | 8.30 us: 1.29x slower                                  |
| deepcopy                 | 371 us                                                 | 479 us: 1.29x slower                                   |
| sqlglot_normalize        | 110 ms                                                 | 143 ms: 1.30x slower                                   |
| chameleon                | 7.41 ms                                                | 9.68 ms: 1.31x slower                                  |
| pprint_safe_repr         | 776 ms                                                 | 1.02 sec: 1.31x slower                                 |
| comprehensions           | 21.8 us                                                | 28.8 us: 1.32x slower                                  |
| tornado_http             | 103 ms                                                 | 136 ms: 1.33x slower                                   |
| pycparser                | 1.18 sec                                               | 1.58 sec: 1.34x slower                                 |
| pprint_pformat           | 1.57 sec                                               | 2.10 sec: 1.34x slower                                 |
| tomli_loads              | 2.33 sec                                               | 3.14 sec: 1.35x slower                                 |
| json_dumps               | 10.4 ms                                                | 14.2 ms: 1.36x slower                                  |
| mako                     | 11.9 ms                                                | 16.3 ms: 1.37x slower                                  |
| float                    | 84.7 ms                                                | 117 ms: 1.38x slower                                   |
| django_template          | 34.6 ms                                                | 48.2 ms: 1.39x slower                                  |
| async_tree_cpu_io_mixed  | 726 ms                                                 | 1.02 sec: 1.40x slower                                 |
| deepcopy_memo            | 40.7 us                                                | 58.5 us: 1.44x slower                                  |
| unpickle_pure_python     | 230 us                                                 | 331 us: 1.44x slower                                   |
| asyncio_tcp_ssl          | 1.79 sec                                               | 2.57 sec: 1.44x slower                                 |
| spectral_norm            | 115 ms                                                 | 170 ms: 1.48x slower                                   |
| pyflate                  | 482 ms                                                 | 716 ms: 1.48x slower                                   |
| scimark_lu               | 118 ms                                                 | 176 ms: 1.49x slower                                   |
| pickle_pure_python       | 324 us                                                 | 484 us: 1.50x slower                                   |
| async_tree_memoization   | 578 ms                                                 | 870 ms: 1.51x slower                                   |
| coroutines               | 23.2 ms                                                | 35.1 ms: 1.51x slower                                  |
| python_startup           | 9.55 ms                                                | 14.6 ms: 1.53x slower                                  |
| sqlglot_transpile        | 1.68 ms                                                | 2.57 ms: 1.53x slower                                  |
| async_tree_io            | 1.16 sec                                               | 1.77 sec: 1.53x slower                                 |
| async_tree_none          | 472 ms                                                 | 728 ms: 1.54x slower                                   |
| crypto_pyaes             | 81.9 ms                                                | 128 ms: 1.56x slower                                   |
| scimark_monte_carlo      | 75.1 ms                                                | 118 ms: 1.57x slower                                   |
| nbody                    | 97.0 ms                                                | 154 ms: 1.58x slower                                   |
| sqlglot_parse            | 1.36 ms                                                | 2.17 ms: 1.59x slower                                  |
| hexiom                   | 6.41 ms                                                | 10.4 ms: 1.62x slower                                  |
| raytrace                 | 312 ms                                                 | 507 ms: 1.62x slower                                   |
| scimark_sor              | 129 ms                                                 | 220 ms: 1.70x slower                                   |
| go                       | 139 ms                                                 | 240 ms: 1.72x slower                                   |
| chaos                    | 67.0 ms                                                | 115 ms: 1.72x slower                                   |
| richards                 | 45.8 ms                                                | 79.3 ms: 1.73x slower                                  |
| logging_silent           | 104 ns                                                 | 190 ns: 1.82x slower                                   |
| richards_super           | 51.5 ms                                                | 94.7 ms: 1.84x slower                                  |
| asyncio_tcp              | 491 ms                                                 | 922 ms: 1.88x slower                                   |
| deltablue                | 3.72 ms                                                | 7.91 ms: 2.13x slower                                  |
| generators               | 31.2 ms                                                | 80.1 ms: 2.57x slower                                  |
| typing_runtime_protocols | 158 us                                                 | 544 us: 3.45x slower                                   |
| Geometric mean           | (ref)                                                  | 1.30x slower                                           |

Benchmark hidden because not significant (3): pickle_list, bench_mp_pool, regex_effbot
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.26x
- 95% likely to have a slowdown of 1.25x
- 99% likely to have a slowdown of 1.23x


# Memory

- memory change: 0.89x