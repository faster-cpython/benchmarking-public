# Results vs. 3.10.4

- fork: colesbury
- ref: gh_100240_freelist
- machine: linux-x86_64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.44x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.33x faster                                                   |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.22x faster                                                 |
| html5lib       | 88.9 ms                                                | 64.9 ms: 1.37x faster                                                  |
| tornado_http   | 136 ms                                                 | 90.0 ms: 1.52x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 318 ms: 2.29x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 400 ms: 2.18x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 820 ms: 2.16x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 562 ms: 1.81x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.10x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.9 ms: 1.77x faster                                                  |
| float          | 117 ms                                                 | 76.7 ms: 1.53x faster                                                  |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.40x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.44x faster                                                   |
| regex_v8       | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                  |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 300 us: 1.62x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.13 sec: 1.48x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 85.6 ms: 1.16x faster                                                  |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                  |
| django_template | 48.2 ms                                                | 33.8 ms: 1.43x faster                                                  |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.38x faster                                                   |
| generators               | 80.1 ms                                                | 29.9 ms: 2.68x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.24 ms: 2.44x faster                                                  |
| async_tree_none          | 728 ms                                                 | 318 ms: 2.29x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 400 ms: 2.18x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 820 ms: 2.16x faster                                                   |
| chaos                    | 115 ms                                                 | 58.4 ms: 1.98x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                                  |
| raytrace                 | 507 ms                                                 | 258 ms: 1.96x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 487 ms: 1.89x faster                                                   |
| logging_silent           | 190 ns                                                 | 101 ns: 1.87x faster                                                   |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                   |
| pylint                   | 551 ms                                                 | 302 ms: 1.83x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 562 ms: 1.81x faster                                                   |
| richards_super           | 94.7 ms                                                | 53.1 ms: 1.79x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 66.4 ms: 1.78x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 72.1 ms: 1.77x faster                                                  |
| nbody                    | 154 ms                                                 | 86.9 ms: 1.77x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                  |
| richards                 | 79.3 ms                                                | 46.6 ms: 1.70x faster                                                  |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                   |
| go                       | 240 ms                                                 | 141 ms: 1.70x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.69x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.16 ms: 1.69x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.62x faster                                                   |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.58x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.56x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                   |
| pyflate                  | 716 ms                                                 | 469 ms: 1.53x faster                                                   |
| float                    | 117 ms                                                 | 76.7 ms: 1.53x faster                                                  |
| tornado_http             | 136 ms                                                 | 90.0 ms: 1.52x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                                  |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                                   |
| logging_format           | 9.09 us                                                | 6.16 us: 1.48x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.13 sec: 1.48x faster                                                 |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                  |
| regex_compile            | 188 ms                                                 | 130 ms: 1.44x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                 |
| django_template          | 48.2 ms                                                | 33.8 ms: 1.43x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.59 ms: 1.41x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 734 ms: 1.39x faster                                                   |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                  |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                  |
| html5lib                 | 88.9 ms                                                | 64.9 ms: 1.37x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.35x faster                                                   |
| thrift                   | 1.07 ms                                                | 797 us: 1.34x faster                                                   |
| nqueens                  | 106 ms                                                 | 79.1 ms: 1.34x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                  |
| 2to3                     | 348 ms                                                 | 261 ms: 1.33x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                  |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 64.4 ms: 1.31x faster                                                  |
| fannkuch                 | 532 ms                                                 | 408 ms: 1.30x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 53.3 ms: 1.30x faster                                                  |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                                  |
| scimark_fft              | 466 ms                                                 | 363 ms: 1.28x faster                                                   |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 786 us: 1.26x faster                                                   |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.22x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 85.6 ms: 1.16x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.14x faster                                                 |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                                  |
| json                     | 5.69 ms                                                | 5.09 ms: 1.12x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                                   |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                   |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                   |
| gc_traversal             | 3.62 ms                                                | 3.53 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| async_generators         | 444 ms                                                 | 438 ms: 1.01x faster                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                  |
| telco                    | 7.27 ms                                                | 8.03 ms: 1.11x slower                                                  |
| coverage                 | 79.4 ms                                                | 91.7 ms: 1.15x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                           |

Benchmark hidden because not significant (3): asyncio_websockets, bench_mp_pool, regex_effbot
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240717-3.14.0a0-85453d0/bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.12x