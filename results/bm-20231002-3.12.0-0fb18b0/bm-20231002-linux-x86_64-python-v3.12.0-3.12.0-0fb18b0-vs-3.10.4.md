
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0
- machine: linux-x86_64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                   |
| chameleon      | 9.68 ms                                                | 7.41 ms: 1.31x faster                                  |
| docutils       | 3.30 sec                                               | 2.77 sec: 1.19x faster                                 |
| tornado_http   | 136 ms                                                 | 103 ms: 1.33x faster                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 472 ms: 1.54x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.16 sec: 1.53x faster                                 |
| async_tree_memoization  | 870 ms                                                 | 578 ms: 1.51x faster                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 726 ms: 1.40x faster                                   |
| Geometric mean          | (ref)                                                  | 1.49x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 154 ms                                                 | 97.0 ms: 1.58x faster                                  |
| float          | 117 ms                                                 | 84.7 ms: 1.38x faster                                  |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 148 ms: 1.27x faster                                   |
| regex_v8       | 27.8 ms                                                | 23.1 ms: 1.20x faster                                  |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                   |
| Geometric mean | (ref)                                                  | 1.13x faster                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 324 us: 1.50x faster                                   |
| unpickle_pure_python | 331 us                                                 | 230 us: 1.44x faster                                   |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                  |
| tomli_loads          | 3.14 sec                                               | 2.33 sec: 1.35x faster                                 |
| xml_etree_process    | 79.1 ms                                                | 61.7 ms: 1.28x faster                                  |
| xml_etree_generate   | 99.4 ms                                                | 89.2 ms: 1.12x faster                                  |
| json_loads           | 31.2 us                                                | 28.5 us: 1.09x faster                                  |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                   |
| xml_etree_parse      | 168 ms                                                 | 159 ms: 1.05x faster                                   |
| unpickle_list        | 5.20 us                                                | 5.29 us: 1.02x slower                                  |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                  |
| unpickle             | 14.4 us                                                | 15.9 us: 1.10x slower                                  |
| pickle_dict          | 29.6 us                                                | 35.5 us: 1.20x slower                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 9.55 ms: 1.53x faster                                  |
| python_startup_no_site | 5.93 ms                                                | 6.94 ms: 1.17x slower                                  |
| Geometric mean         | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 48.2 ms                                                | 34.6 ms: 1.39x faster                                  |
| mako            | 16.3 ms                                                | 11.9 ms: 1.37x faster                                  |
| Geometric mean  | (ref)                                                  | 1.38x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 158 us: 3.45x faster                                   |
| generators               | 80.1 ms                                                | 31.2 ms: 2.57x faster                                  |
| deltablue                | 7.91 ms                                                | 3.72 ms: 2.13x faster                                  |
| asyncio_tcp              | 922 ms                                                 | 491 ms: 1.88x faster                                   |
| richards_super           | 94.7 ms                                                | 51.5 ms: 1.84x faster                                  |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                   |
| richards                 | 79.3 ms                                                | 45.8 ms: 1.73x faster                                  |
| chaos                    | 115 ms                                                 | 67.0 ms: 1.72x faster                                  |
| go                       | 240 ms                                                 | 139 ms: 1.72x faster                                   |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                   |
| raytrace                 | 507 ms                                                 | 312 ms: 1.62x faster                                   |
| hexiom                   | 10.4 ms                                                | 6.41 ms: 1.62x faster                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.36 ms: 1.59x faster                                  |
| nbody                    | 154 ms                                                 | 97.0 ms: 1.58x faster                                  |
| scimark_monte_carlo      | 118 ms                                                 | 75.1 ms: 1.57x faster                                  |
| crypto_pyaes             | 128 ms                                                 | 81.9 ms: 1.56x faster                                  |
| async_tree_none          | 728 ms                                                 | 472 ms: 1.54x faster                                   |
| async_tree_io            | 1.77 sec                                               | 1.16 sec: 1.53x faster                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.68 ms: 1.53x faster                                  |
| python_startup           | 14.6 ms                                                | 9.55 ms: 1.53x faster                                  |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                  |
| async_tree_memoization   | 870 ms                                                 | 578 ms: 1.51x faster                                   |
| pickle_pure_python       | 484 us                                                 | 324 us: 1.50x faster                                   |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                   |
| pyflate                  | 716 ms                                                 | 482 ms: 1.48x faster                                   |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                 |
| unpickle_pure_python     | 331 us                                                 | 230 us: 1.44x faster                                   |
| deepcopy_memo            | 58.5 us                                                | 40.7 us: 1.44x faster                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 726 ms: 1.40x faster                                   |
| django_template          | 48.2 ms                                                | 34.6 ms: 1.39x faster                                  |
| float                    | 117 ms                                                 | 84.7 ms: 1.38x faster                                  |
| mako                     | 16.3 ms                                                | 11.9 ms: 1.37x faster                                  |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                  |
| tomli_loads              | 3.14 sec                                               | 2.33 sec: 1.35x faster                                 |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                 |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                 |
| tornado_http             | 136 ms                                                 | 103 ms: 1.33x faster                                   |
| comprehensions           | 28.8 us                                                | 21.8 us: 1.32x faster                                  |
| pprint_safe_repr         | 1.02 sec                                               | 776 ms: 1.31x faster                                   |
| chameleon                | 9.68 ms                                                | 7.41 ms: 1.31x faster                                  |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                   |
| deepcopy                 | 479 us                                                 | 371 us: 1.29x faster                                   |
| logging_simple           | 8.30 us                                                | 6.46 us: 1.29x faster                                  |
| xml_etree_process        | 79.1 ms                                                | 61.7 ms: 1.28x faster                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.06 ms: 1.28x faster                                  |
| fannkuch                 | 532 ms                                                 | 417 ms: 1.27x faster                                   |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                   |
| nqueens                  | 106 ms                                                 | 83.3 ms: 1.27x faster                                  |
| regex_compile            | 188 ms                                                 | 148 ms: 1.27x faster                                   |
| sqlglot_optimize         | 69.2 ms                                                | 54.8 ms: 1.26x faster                                  |
| logging_format           | 9.09 us                                                | 7.23 us: 1.26x faster                                  |
| aiohttp                  | 1.44 ms                                                | 1.15 ms: 1.25x faster                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 18.7 ms: 1.25x faster                                  |
| deepcopy_reduce          | 4.17 us                                                | 3.35 us: 1.25x faster                                  |
| gunicorn                 | 1.53 ms                                                | 1.24 ms: 1.23x faster                                  |
| dulwich_log              | 84.3 ms                                                | 68.5 ms: 1.23x faster                                  |
| scimark_fft              | 466 ms                                                 | 382 ms: 1.22x faster                                   |
| sympy_integrate          | 25.8 ms                                                | 21.4 ms: 1.20x faster                                  |
| regex_v8                 | 27.8 ms                                                | 23.1 ms: 1.20x faster                                  |
| docutils                 | 3.30 sec                                               | 2.77 sec: 1.19x faster                                 |
| dask                     | 441 ms                                                 | 372 ms: 1.19x faster                                   |
| sympy_expand             | 566 ms                                                 | 478 ms: 1.18x faster                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 147 ms: 1.17x faster                                   |
| bench_thread_pool        | 986 us                                                 | 842 us: 1.17x faster                                   |
| sympy_sum                | 196 ms                                                 | 169 ms: 1.16x faster                                   |
| sympy_str                | 346 ms                                                 | 300 ms: 1.15x faster                                   |
| xml_etree_generate       | 99.4 ms                                                | 89.2 ms: 1.12x faster                                  |
| unpack_sequence          | 60.0 ns                                                | 54.0 ns: 1.11x faster                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.48 ms: 1.10x faster                                  |
| json_loads               | 31.2 us                                                | 28.5 us: 1.09x faster                                  |
| coverage                 | 79.4 ms                                                | 72.7 ms: 1.09x faster                                  |
| mdp                      | 2.85 sec                                               | 2.63 sec: 1.08x faster                                 |
| json                     | 5.69 ms                                                | 5.26 ms: 1.08x faster                                  |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                   |
| mypy2                    | 894 ms                                                 | 830 ms: 1.08x faster                                   |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                   |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                  |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.06x faster                                   |
| pathlib                  | 20.5 ms                                                | 19.3 ms: 1.06x faster                                  |
| xml_etree_parse          | 168 ms                                                 | 159 ms: 1.05x faster                                   |
| telco                    | 7.27 ms                                                | 7.10 ms: 1.02x faster                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                   |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                   |
| unpickle_list            | 5.20 us                                                | 5.29 us: 1.02x slower                                  |
| async_generators         | 444 ms                                                 | 463 ms: 1.04x slower                                   |
| gc_traversal             | 3.62 ms                                                | 3.79 ms: 1.05x slower                                  |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                  |
| unpickle                 | 14.4 us                                                | 15.9 us: 1.10x slower                                  |
| python_startup_no_site   | 5.93 ms                                                | 6.94 ms: 1.17x slower                                  |
| pickle_dict              | 29.6 us                                                | 35.5 us: 1.20x slower                                  |
| Geometric mean           | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (3): regex_effbot, bench_mp_pool, pickle_list
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x


# Memory

- memory change: 1.15x