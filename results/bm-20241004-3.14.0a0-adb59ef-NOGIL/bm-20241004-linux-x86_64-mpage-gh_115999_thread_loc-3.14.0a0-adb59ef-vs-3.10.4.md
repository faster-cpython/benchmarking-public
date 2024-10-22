# Results vs. 3.10.4

- fork: mpage
- ref: gh_115999_thread_loc
- machine: linux-x86_64
- commit hash: adb59ef
- commit date: 2024-10-04
- overall geometric mean: 1.05x slower
- HPT reliability: 97.64%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 393 ms: 1.13x slower                                                 |
| docutils       | 3.30 sec                                               | 3.24 sec: 1.02x faster                                               |
| html5lib       | 88.9 ms                                                | 93.9 ms: 1.06x slower                                                |
| tornado_http   | 136 ms                                                 | 138 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 897 ms: 1.97x faster                                                 |
| async_tree_none         | 728 ms                                                 | 402 ms: 1.81x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 505 ms: 1.72x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 656 ms: 1.55x faster                                                 |
| Geometric mean          | (ref)                                                  | 1.76x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 191 ms                                                 | 183 ms: 1.04x faster                                                 |
| float          | 117 ms                                                 | 137 ms: 1.17x slower                                                 |
| nbody          | 154 ms                                                 | 189 ms: 1.23x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 25.8 ms: 1.08x faster                                                |
| regex_dna      | 227 ms                                                 | 217 ms: 1.04x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.54 ms: 1.03x faster                                                |
| regex_compile  | 188 ms                                                 | 213 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                 |
| json_dumps           | 14.2 ms                                                | 12.8 ms: 1.10x faster                                                |
| pickle_list          | 5.08 us                                                | 4.75 us: 1.07x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 112 ms: 1.03x faster                                                 |
| json_loads           | 31.2 us                                                | 30.3 us: 1.03x faster                                                |
| pickle               | 10.7 us                                                | 10.7 us: 1.00x slower                                                |
| tomli_loads          | 3.14 sec                                               | 3.17 sec: 1.01x slower                                               |
| unpickle_list        | 5.20 us                                                | 5.49 us: 1.06x slower                                                |
| xml_etree_generate   | 99.4 ms                                                | 108 ms: 1.09x slower                                                 |
| xml_etree_process    | 79.1 ms                                                | 86.8 ms: 1.10x slower                                                |
| unpickle             | 14.4 us                                                | 15.9 us: 1.11x slower                                                |
| pickle_dict          | 29.6 us                                                | 33.0 us: 1.12x slower                                                |
| pickle_pure_python   | 484 us                                                 | 564 us: 1.16x slower                                                 |
| unpickle_pure_python | 331 us                                                 | 390 us: 1.18x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 14.3 ms: 1.02x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 9.52 ms: 1.61x slower                                                |
| Geometric mean         | (ref)                                                  | 1.25x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 59.7 ms: 1.24x slower                                                |
| genshi_text     | 31.8 ms                                                | 39.9 ms: 1.25x slower                                                |
| genshi_xml      | 66.0 ms                                                | 83.2 ms: 1.26x slower                                                |
| mako            | 16.3 ms                                                | 20.7 ms: 1.27x slower                                                |
| Geometric mean  | (ref)                                                  | 1.26x slower                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 246 us: 2.21x faster                                                 |
| generators               | 80.1 ms                                                | 38.0 ms: 2.11x faster                                                |
| async_tree_io            | 1.77 sec                                               | 897 ms: 1.97x faster                                                 |
| async_tree_none          | 728 ms                                                 | 402 ms: 1.81x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 505 ms: 1.72x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 558 ms: 1.65x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 656 ms: 1.55x faster                                                 |
| pylint                   | 551 ms                                                 | 394 ms: 1.40x faster                                                 |
| gc_traversal             | 3.62 ms                                                | 2.90 ms: 1.25x faster                                                |
| asyncio_tcp_ssl          | 2.57 sec                                               | 2.07 sec: 1.24x faster                                               |
| deepcopy                 | 479 us                                                 | 408 us: 1.17x faster                                                 |
| coroutines               | 35.1 ms                                                | 30.1 ms: 1.16x faster                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.39 ms: 1.16x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 110 ms: 1.16x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 51.4 us: 1.14x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                 |
| json_dumps               | 14.2 ms                                                | 12.8 ms: 1.10x faster                                                |
| scimark_fft              | 466 ms                                                 | 422 ms: 1.10x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.88 ms: 1.10x faster                                                |
| regex_v8                 | 27.8 ms                                                | 25.8 ms: 1.08x faster                                                |
| pathlib                  | 20.5 ms                                                | 19.1 ms: 1.07x faster                                                |
| pickle_list              | 5.08 us                                                | 4.75 us: 1.07x faster                                                |
| regex_dna                | 227 ms                                                 | 217 ms: 1.04x faster                                                 |
| spectral_norm            | 170 ms                                                 | 163 ms: 1.04x faster                                                 |
| pidigits                 | 191 ms                                                 | 183 ms: 1.04x faster                                                 |
| chaos                    | 115 ms                                                 | 112 ms: 1.03x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 112 ms: 1.03x faster                                                 |
| json_loads               | 31.2 us                                                | 30.3 us: 1.03x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.54 ms: 1.03x faster                                                |
| python_startup           | 14.6 ms                                                | 14.3 ms: 1.02x faster                                                |
| docutils                 | 3.30 sec                                               | 3.24 sec: 1.02x faster                                               |
| richards                 | 79.3 ms                                                | 78.0 ms: 1.02x faster                                                |
| json                     | 5.69 ms                                                | 5.60 ms: 1.02x faster                                                |
| comprehensions           | 28.8 us                                                | 28.4 us: 1.01x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                 |
| pickle                   | 10.7 us                                                | 10.7 us: 1.00x slower                                                |
| richards_super           | 94.7 ms                                                | 95.6 ms: 1.01x slower                                                |
| tomli_loads              | 3.14 sec                                               | 3.17 sec: 1.01x slower                                               |
| tornado_http             | 136 ms                                                 | 138 ms: 1.01x slower                                                 |
| deepcopy_reduce          | 4.17 us                                                | 4.23 us: 1.02x slower                                                |
| pycparser                | 1.58 sec                                               | 1.60 sec: 1.02x slower                                               |
| logging_silent           | 190 ns                                                 | 195 ns: 1.03x slower                                                 |
| sqlite_synth             | 3.02 us                                                | 3.14 us: 1.04x slower                                                |
| deltablue                | 7.91 ms                                                | 8.21 ms: 1.04x slower                                                |
| dulwich_log              | 84.3 ms                                                | 87.6 ms: 1.04x slower                                                |
| pyflate                  | 716 ms                                                 | 751 ms: 1.05x slower                                                 |
| html5lib                 | 88.9 ms                                                | 93.9 ms: 1.06x slower                                                |
| unpickle_list            | 5.20 us                                                | 5.49 us: 1.06x slower                                                |
| nqueens                  | 106 ms                                                 | 114 ms: 1.08x slower                                                 |
| xml_etree_generate       | 99.4 ms                                                | 108 ms: 1.09x slower                                                 |
| xml_etree_process        | 79.1 ms                                                | 86.8 ms: 1.10x slower                                                |
| fannkuch                 | 532 ms                                                 | 585 ms: 1.10x slower                                                 |
| unpickle                 | 14.4 us                                                | 15.9 us: 1.11x slower                                                |
| go                       | 240 ms                                                 | 267 ms: 1.11x slower                                                 |
| raytrace                 | 507 ms                                                 | 564 ms: 1.11x slower                                                 |
| pickle_dict              | 29.6 us                                                | 33.0 us: 1.12x slower                                                |
| 2to3                     | 348 ms                                                 | 393 ms: 1.13x slower                                                 |
| regex_compile            | 188 ms                                                 | 213 ms: 1.13x slower                                                 |
| hexiom                   | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                |
| sympy_integrate          | 25.8 ms                                                | 29.4 ms: 1.14x slower                                                |
| thrift                   | 1.07 ms                                                | 1.22 ms: 1.14x slower                                                |
| scimark_sor              | 220 ms                                                 | 251 ms: 1.14x slower                                                 |
| mdp                      | 2.85 sec                                               | 3.32 sec: 1.16x slower                                               |
| pickle_pure_python       | 484 us                                                 | 564 us: 1.16x slower                                                 |
| float                    | 117 ms                                                 | 137 ms: 1.17x slower                                                 |
| sqlglot_normalize        | 143 ms                                                 | 168 ms: 1.18x slower                                                 |
| meteor_contest           | 120 ms                                                 | 141 ms: 1.18x slower                                                 |
| unpickle_pure_python     | 331 us                                                 | 390 us: 1.18x slower                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 3.07 ms: 1.19x slower                                                |
| async_generators         | 444 ms                                                 | 531 ms: 1.20x slower                                                 |
| sqlglot_parse            | 2.17 ms                                                | 2.60 ms: 1.20x slower                                                |
| sqlglot_optimize         | 69.2 ms                                                | 84.5 ms: 1.22x slower                                                |
| pprint_pformat           | 2.10 sec                                               | 2.58 sec: 1.22x slower                                               |
| nbody                    | 154 ms                                                 | 189 ms: 1.23x slower                                                 |
| logging_simple           | 8.30 us                                                | 10.2 us: 1.23x slower                                                |
| pprint_safe_repr         | 1.02 sec                                               | 1.25 sec: 1.23x slower                                               |
| logging_format           | 9.09 us                                                | 11.2 us: 1.24x slower                                                |
| django_template          | 48.2 ms                                                | 59.7 ms: 1.24x slower                                                |
| sympy_str                | 346 ms                                                 | 429 ms: 1.24x slower                                                 |
| genshi_text              | 31.8 ms                                                | 39.9 ms: 1.25x slower                                                |
| scimark_lu               | 176 ms                                                 | 221 ms: 1.26x slower                                                 |
| genshi_xml               | 66.0 ms                                                | 83.2 ms: 1.26x slower                                                |
| mako                     | 16.3 ms                                                | 20.7 ms: 1.27x slower                                                |
| sympy_expand             | 566 ms                                                 | 758 ms: 1.34x slower                                                 |
| sympy_sum                | 196 ms                                                 | 265 ms: 1.35x slower                                                 |
| coverage                 | 79.4 ms                                                | 108 ms: 1.36x slower                                                 |
| telco                    | 7.27 ms                                                | 9.92 ms: 1.36x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 9.52 ms: 1.61x slower                                                |
| unpack_sequence          | 60.0 ns                                                | 150 ns: 2.51x slower                                                 |
| bench_mp_pool            | 24.0 ms                                                | 66.3 ms: 2.76x slower                                                |
| bench_thread_pool        | 986 us                                                 | 3.44 ms: 3.49x slower                                                |
| Geometric mean           | (ref)                                                  | 1.05x slower                                                         |

Benchmark hidden because not significant (1): scimark_monte_carlo
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241004-3.14.0a0-adb59ef-NOGIL/bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 97.64% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.31x