# Results vs. 3.10.4

- fork: python
- ref: a4fd7aa4a6420cef1c22
- machine: linux-x86_64
- commit hash: a4fd7aa
- commit date: 2024-08-21
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 264 ms: 1.32x faster                                                  |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                |
| html5lib       | 88.9 ms                                                | 63.6 ms: 1.40x faster                                                 |
| tornado_http   | 136 ms                                                 | 90.5 ms: 1.51x faster                                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 394 ms: 2.21x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 936 ms: 1.89x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.80x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.7 ms: 1.77x faster                                                 |
| float          | 117 ms                                                 | 78.1 ms: 1.50x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.40x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.47x faster                                                  |
| regex_v8       | 27.8 ms                                                | 26.2 ms: 1.06x faster                                                 |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 306 us: 1.58x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.0 ms: 1.17x faster                                                 |
| json_loads           | 31.2 us                                                | 28.4 us: 1.10x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 155 ms: 1.08x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                 |
| django_template | 48.2 ms                                                | 33.8 ms: 1.42x faster                                                 |
| genshi_text     | 31.8 ms                                                | 22.5 ms: 1.41x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.35x faster                                                  |
| generators               | 80.1 ms                                                | 28.1 ms: 2.85x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.43x faster                                                 |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 394 ms: 2.21x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 474 ms: 1.94x faster                                                  |
| chaos                    | 115 ms                                                 | 59.6 ms: 1.94x faster                                                 |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 936 ms: 1.89x faster                                                  |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                  |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.80x faster                                                  |
| richards_super           | 94.7 ms                                                | 53.3 ms: 1.78x faster                                                 |
| nbody                    | 154 ms                                                 | 86.7 ms: 1.77x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 72.5 ms: 1.76x faster                                                 |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 68.3 ms: 1.73x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                 |
| pylint                   | 551 ms                                                 | 320 ms: 1.72x faster                                                  |
| go                       | 240 ms                                                 | 142 ms: 1.69x faster                                                  |
| richards                 | 79.3 ms                                                | 47.4 ms: 1.67x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.66x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.30 ms: 1.65x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 306 us: 1.58x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                 |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                  |
| pyflate                  | 716 ms                                                 | 466 ms: 1.54x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.47 us: 1.52x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                |
| tornado_http             | 136 ms                                                 | 90.5 ms: 1.51x faster                                                 |
| float                    | 117 ms                                                 | 78.1 ms: 1.50x faster                                                 |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.48x faster                                                  |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                 |
| regex_compile            | 188 ms                                                 | 129 ms: 1.47x faster                                                  |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                                |
| django_template          | 48.2 ms                                                | 33.8 ms: 1.42x faster                                                 |
| genshi_text              | 31.8 ms                                                | 22.5 ms: 1.41x faster                                                 |
| html5lib                 | 88.9 ms                                                | 63.6 ms: 1.40x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| thrift                   | 1.07 ms                                                | 779 us: 1.38x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 743 ms: 1.37x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                                  |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                  |
| nqueens                  | 106 ms                                                 | 79.7 ms: 1.33x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                                |
| genshi_xml               | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                 |
| 2to3                     | 348 ms                                                 | 264 ms: 1.32x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.92 ms: 1.32x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                 |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 53.4 ms: 1.30x faster                                                 |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                 |
| scimark_fft              | 466 ms                                                 | 368 ms: 1.26x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 789 us: 1.25x faster                                                  |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 85.0 ms: 1.17x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.13x faster                                                |
| json_loads               | 31.2 us                                                | 28.4 us: 1.10x faster                                                 |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 155 ms: 1.08x faster                                                  |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 26.2 ms: 1.06x faster                                                 |
| async_generators         | 444 ms                                                 | 432 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 3.86 ms: 1.06x slower                                                 |
| coverage                 | 79.4 ms                                                | 85.7 ms: 1.08x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                 |
| telco                    | 7.27 ms                                                | 8.16 ms: 1.12x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240821-3.14.0a0-a4fd7aa/bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.12x