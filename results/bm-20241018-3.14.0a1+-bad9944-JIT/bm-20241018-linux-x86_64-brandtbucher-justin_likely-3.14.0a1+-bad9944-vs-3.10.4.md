# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_likely
- machine: linux-x86_64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 278 ms: 1.25x faster                                                  |
| docutils       | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                |
| html5lib       | 88.9 ms                                                | 64.0 ms: 1.39x faster                                                 |
| tornado_http   | 136 ms                                                 | 95.0 ms: 1.44x faster                                                 |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 329 ms: 2.21x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 420 ms: 2.07x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 854 ms: 2.07x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 572 ms: 1.78x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 84.5 ms: 1.82x faster                                                 |
| float          | 117 ms                                                 | 76.0 ms: 1.54x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.42x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.32x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                 |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                |
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.51x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 55.5 ms: 1.43x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 78.8 ms: 1.26x faster                                                 |
| json_loads           | 31.2 us                                                | 26.5 us: 1.18x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 99.7 ms: 1.16x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.13 us: 1.01x slower                                                 |
| unpickle_list        | 5.20 us                                                | 5.53 us: 1.06x slower                                                 |
| pickle               | 10.7 us                                                | 11.9 us: 1.11x slower                                                 |
| pickle_dict          | 29.6 us                                                | 34.8 us: 1.18x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.9 ms: 1.23x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                 |
| django_template | 48.2 ms                                                | 36.7 ms: 1.31x faster                                                 |
| genshi_text     | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 61.9 ms: 1.07x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.27x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                 |
| generators               | 80.1 ms                                                | 35.2 ms: 2.28x faster                                                 |
| async_tree_none          | 728 ms                                                 | 329 ms: 2.21x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 420 ms: 2.07x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 854 ms: 2.07x faster                                                  |
| richards_super           | 94.7 ms                                                | 47.2 ms: 2.01x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                                 |
| chaos                    | 115 ms                                                 | 59.4 ms: 1.94x faster                                                 |
| logging_silent           | 190 ns                                                 | 98.8 ns: 1.92x faster                                                 |
| richards                 | 79.3 ms                                                | 41.4 ms: 1.92x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 67.7 ms: 1.89x faster                                                 |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 63.9 ms: 1.85x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 499 ms: 1.85x faster                                                  |
| raytrace                 | 507 ms                                                 | 278 ms: 1.82x faster                                                  |
| nbody                    | 154 ms                                                 | 84.5 ms: 1.82x faster                                                 |
| go                       | 240 ms                                                 | 134 ms: 1.79x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 572 ms: 1.78x faster                                                  |
| deepcopy                 | 479 us                                                 | 274 us: 1.75x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.4 us: 1.65x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                                 |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                 |
| pyflate                  | 716 ms                                                 | 455 ms: 1.58x faster                                                  |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                                  |
| float                    | 117 ms                                                 | 76.0 ms: 1.54x faster                                                 |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.52x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.51x faster                                                  |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.51x faster                                                  |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.81 us: 1.48x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                 |
| hexiom                   | 10.4 ms                                                | 7.07 ms: 1.47x faster                                                 |
| pylint                   | 551 ms                                                 | 377 ms: 1.46x faster                                                  |
| scimark_fft              | 466 ms                                                 | 323 ms: 1.44x faster                                                  |
| tornado_http             | 136 ms                                                 | 95.0 ms: 1.44x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 55.5 ms: 1.43x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.42x faster                                                |
| html5lib                 | 88.9 ms                                                | 64.0 ms: 1.39x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 742 ms: 1.37x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                |
| thrift                   | 1.07 ms                                                | 794 us: 1.35x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.33x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.90 ms: 1.32x faster                                                 |
| regex_compile            | 188 ms                                                 | 143 ms: 1.32x faster                                                  |
| django_template          | 48.2 ms                                                | 36.7 ms: 1.31x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 66.7 ms: 1.26x faster                                                 |
| genshi_text              | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 78.8 ms: 1.26x faster                                                 |
| 2to3                     | 348 ms                                                 | 278 ms: 1.25x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.24x faster                                                  |
| python_startup           | 14.6 ms                                                | 11.9 ms: 1.23x faster                                                 |
| nqueens                  | 106 ms                                                 | 88.6 ms: 1.19x faster                                                 |
| json_loads               | 31.2 us                                                | 26.5 us: 1.18x faster                                                 |
| json                     | 5.69 ms                                                | 4.88 ms: 1.17x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 99.7 ms: 1.16x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 60.6 ms: 1.14x faster                                                 |
| sympy_str                | 346 ms                                                 | 303 ms: 1.14x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 878 us: 1.12x faster                                                  |
| sympy_expand             | 566 ms                                                 | 505 ms: 1.12x faster                                                  |
| sympy_sum                | 196 ms                                                 | 175 ms: 1.12x faster                                                  |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 23.6 ms: 1.09x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 61.9 ms: 1.07x faster                                                 |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.75 sec: 1.03x faster                                                |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                  |
| pickle_list              | 5.08 us                                                | 5.13 us: 1.01x slower                                                 |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                                  |
| telco                    | 7.27 ms                                                | 7.69 ms: 1.06x slower                                                 |
| unpickle_list            | 5.20 us                                                | 5.53 us: 1.06x slower                                                 |
| coverage                 | 79.4 ms                                                | 84.6 ms: 1.06x slower                                                 |
| pickle                   | 10.7 us                                                | 11.9 us: 1.11x slower                                                 |
| pickle_dict              | 29.6 us                                                | 34.8 us: 1.18x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.52 ms: 1.25x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.68 ms: 1.65x slower                                                 |
| unpack_sequence          | 60.0 ns                                                | 108 ns: 1.81x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 84.0 ms: 3.50x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                          |

Benchmark hidden because not significant (2): unpickle, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.32x