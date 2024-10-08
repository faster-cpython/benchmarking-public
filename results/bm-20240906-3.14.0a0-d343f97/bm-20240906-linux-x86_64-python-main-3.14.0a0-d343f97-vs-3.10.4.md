# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: d343f97
- commit date: 2024-09-06
- overall geometric mean: 1.39x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                  |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                 |
| tornado_http   | 136 ms                                                 | 91.6 ms: 1.49x faster                                 |
| Geometric mean | (ref)                                                  | 1.38x faster                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 323 ms: 2.25x faster                                  |
| async_tree_memoization  | 870 ms                                                 | 387 ms: 2.25x faster                                  |
| async_tree_io           | 1.77 sec                                               | 927 ms: 1.91x faster                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 555 ms: 1.83x faster                                  |
| Geometric mean          | (ref)                                                  | 2.05x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.3 ms: 1.78x faster                                 |
| float          | 117 ms                                                 | 77.8 ms: 1.50x faster                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.40x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                  |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                 |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 300 us: 1.61x faster                                  |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.55x faster                                  |
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                 |
| xml_etree_process    | 79.1 ms                                                | 58.6 ms: 1.35x faster                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.2 ms: 1.17x faster                                 |
| json_loads           | 31.2 us                                                | 28.4 us: 1.10x faster                                 |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                  |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                  |
| pickle_list          | 5.08 us                                                | 5.16 us: 1.02x slower                                 |
| unpickle             | 14.4 us                                                | 15.2 us: 1.06x slower                                 |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                 |
| pickle_dict          | 29.6 us                                                | 35.4 us: 1.20x slower                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                 |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                 |
| genshi_text     | 31.8 ms                                                | 22.1 ms: 1.44x faster                                 |
| django_template | 48.2 ms                                                | 34.2 ms: 1.41x faster                                 |
| genshi_xml      | 66.0 ms                                                | 48.7 ms: 1.36x faster                                 |
| Geometric mean  | (ref)                                                  | 1.42x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.42x faster                                  |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                 |
| deltablue                | 7.91 ms                                                | 3.21 ms: 2.47x faster                                 |
| async_tree_none          | 728 ms                                                 | 323 ms: 2.25x faster                                  |
| async_tree_memoization   | 870 ms                                                 | 387 ms: 2.25x faster                                  |
| go                       | 240 ms                                                 | 118 ms: 2.04x faster                                  |
| chaos                    | 115 ms                                                 | 58.5 ms: 1.97x faster                                 |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                 |
| raytrace                 | 507 ms                                                 | 260 ms: 1.95x faster                                  |
| asyncio_tcp              | 922 ms                                                 | 481 ms: 1.92x faster                                  |
| async_tree_io            | 1.77 sec                                               | 927 ms: 1.91x faster                                  |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                  |
| logging_silent           | 190 ns                                                 | 103 ns: 1.85x faster                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 555 ms: 1.83x faster                                  |
| richards_super           | 94.7 ms                                                | 52.5 ms: 1.80x faster                                 |
| nbody                    | 154 ms                                                 | 86.3 ms: 1.78x faster                                 |
| scimark_monte_carlo      | 118 ms                                                 | 67.4 ms: 1.75x faster                                 |
| crypto_pyaes             | 128 ms                                                 | 73.1 ms: 1.75x faster                                 |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.75x faster                                  |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                 |
| pylint                   | 551 ms                                                 | 322 ms: 1.71x faster                                  |
| richards                 | 79.3 ms                                                | 46.5 ms: 1.71x faster                                 |
| hexiom                   | 10.4 ms                                                | 6.14 ms: 1.69x faster                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.69x faster                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                 |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.61x faster                                  |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.57x faster                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                 |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.55x faster                                  |
| pyflate                  | 716 ms                                                 | 475 ms: 1.51x faster                                  |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                 |
| float                    | 117 ms                                                 | 77.8 ms: 1.50x faster                                 |
| tornado_http             | 136 ms                                                 | 91.6 ms: 1.49x faster                                 |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                  |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                 |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                  |
| logging_format           | 9.09 us                                                | 6.26 us: 1.45x faster                                 |
| logging_simple           | 8.30 us                                                | 5.77 us: 1.44x faster                                 |
| genshi_text              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                 |
| pprint_safe_repr         | 1.02 sec                                               | 713 ms: 1.43x faster                                  |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                |
| django_template          | 48.2 ms                                                | 34.2 ms: 1.41x faster                                 |
| thrift                   | 1.07 ms                                                | 772 us: 1.39x faster                                  |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                 |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                  |
| genshi_xml               | 66.0 ms                                                | 48.7 ms: 1.36x faster                                 |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                 |
| xml_etree_process        | 79.1 ms                                                | 58.6 ms: 1.35x faster                                 |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.83 ms: 1.34x faster                                 |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.32x faster                                  |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                 |
| dulwich_log              | 84.3 ms                                                | 64.6 ms: 1.31x faster                                 |
| nqueens                  | 106 ms                                                 | 81.2 ms: 1.30x faster                                 |
| sqlglot_optimize         | 69.2 ms                                                | 53.3 ms: 1.30x faster                                 |
| fannkuch                 | 532 ms                                                 | 410 ms: 1.30x faster                                  |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                  |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                 |
| scimark_fft              | 466 ms                                                 | 363 ms: 1.28x faster                                  |
| bench_thread_pool        | 986 us                                                 | 790 us: 1.25x faster                                  |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                  |
| unpack_sequence          | 60.0 ns                                                | 50.4 ns: 1.19x faster                                 |
| xml_etree_generate       | 99.4 ms                                                | 85.2 ms: 1.17x faster                                 |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                 |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                  |
| json_loads               | 31.2 us                                                | 28.4 us: 1.10x faster                                 |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                  |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                  |
| json                     | 5.69 ms                                                | 5.35 ms: 1.06x faster                                 |
| sqlite_synth             | 3.02 us                                                | 2.89 us: 1.04x faster                                 |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                  |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                  |
| gc_traversal             | 3.62 ms                                                | 3.56 ms: 1.02x faster                                 |
| async_generators         | 444 ms                                                 | 439 ms: 1.01x faster                                  |
| pickle_list              | 5.08 us                                                | 5.16 us: 1.02x slower                                 |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.06x slower                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.72 ms: 1.06x slower                                 |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                 |
| coverage                 | 79.4 ms                                                | 86.6 ms: 1.09x slower                                 |
| telco                    | 7.27 ms                                                | 8.27 ms: 1.14x slower                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                 |
| pickle_dict              | 29.6 us                                                | 35.4 us: 1.20x slower                                 |
| Geometric mean           | (ref)                                                  | 1.39x faster                                          |

Benchmark hidden because not significant (4): asyncio_websockets, regex_effbot, bench_mp_pool, unpickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240906-3.14.0a0-d343f97/bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.12x