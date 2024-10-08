# Results vs. 3.10.4

- fork: colesbury
- ref: gh_117376_pydecref_m
- machine: linux-x86_64
- commit hash: 4b27f3a
- commit date: 2024-08-13
- overall geometric mean: 1.05x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 395 ms: 1.13x slower                                                     |
| docutils       | 3.30 sec                                               | 3.33 sec: 1.01x slower                                                   |
| html5lib       | 88.9 ms                                                | 98.6 ms: 1.11x slower                                                    |
| tornado_http   | 136 ms                                                 | 139 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.07x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 892 ms: 1.98x faster                                                     |
| async_tree_none         | 728 ms                                                 | 406 ms: 1.80x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 510 ms: 1.71x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 659 ms: 1.54x faster                                                     |
| Geometric mean          | (ref)                                                  | 1.75x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                 | 184 ms: 1.04x faster                                                     |
| float          | 117 ms                                                 | 139 ms: 1.19x slower                                                     |
| nbody          | 154 ms                                                 | 223 ms: 1.45x slower                                                     |
| Geometric mean | (ref)                                                  | 1.19x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                    |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.54 ms: 1.03x faster                                                    |
| regex_compile  | 188 ms                                                 | 217 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 168 ms                                                 | 153 ms: 1.10x faster                                                     |
| json_dumps           | 14.2 ms                                                | 13.6 ms: 1.04x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 114 ms: 1.02x faster                                                     |
| json_loads           | 31.2 us                                                | 31.6 us: 1.01x slower                                                    |
| tomli_loads          | 3.14 sec                                               | 3.22 sec: 1.03x slower                                                   |
| xml_etree_generate   | 99.4 ms                                                | 110 ms: 1.11x slower                                                     |
| xml_etree_process    | 79.1 ms                                                | 88.3 ms: 1.12x slower                                                    |
| pickle_pure_python   | 484 us                                                 | 575 us: 1.19x slower                                                     |
| unpickle_pure_python | 331 us                                                 | 408 us: 1.23x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.7 ms: 1.06x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 9.30 ms: 1.57x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.21x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 59.8 ms: 1.24x slower                                                    |
| genshi_xml      | 66.0 ms                                                | 82.4 ms: 1.25x slower                                                    |
| genshi_text     | 31.8 ms                                                | 39.9 ms: 1.25x slower                                                    |
| mako            | 16.3 ms                                                | 21.1 ms: 1.30x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.26x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| generators               | 80.1 ms                                                | 36.4 ms: 2.20x faster                                                    |
| typing_runtime_protocols | 544 us                                                 | 251 us: 2.17x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 892 ms: 1.98x faster                                                     |
| async_tree_none          | 728 ms                                                 | 406 ms: 1.80x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 510 ms: 1.71x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 568 ms: 1.62x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 659 ms: 1.54x faster                                                     |
| pylint                   | 551 ms                                                 | 392 ms: 1.41x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 2.05 sec: 1.26x faster                                                   |
| gc_traversal             | 3.62 ms                                                | 3.03 ms: 1.20x faster                                                    |
| create_gc_cycles         | 1.62 ms                                                | 1.38 ms: 1.17x faster                                                    |
| deepcopy                 | 479 us                                                 | 421 us: 1.14x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 113 ms: 1.13x faster                                                     |
| coroutines               | 35.1 ms                                                | 31.6 ms: 1.11x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 53.2 us: 1.10x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 153 ms: 1.10x faster                                                     |
| pathlib                  | 20.5 ms                                                | 18.9 ms: 1.08x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                    |
| python_startup           | 14.6 ms                                                | 13.7 ms: 1.06x faster                                                    |
| json_dumps               | 14.2 ms                                                | 13.6 ms: 1.04x faster                                                    |
| pidigits                 | 191 ms                                                 | 184 ms: 1.04x faster                                                     |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                     |
| regex_effbot             | 3.63 ms                                                | 3.54 ms: 1.03x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 114 ms: 1.02x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                     |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                    |
| docutils                 | 3.30 sec                                               | 3.33 sec: 1.01x slower                                                   |
| richards                 | 79.3 ms                                                | 80.1 ms: 1.01x slower                                                    |
| json_loads               | 31.2 us                                                | 31.6 us: 1.01x slower                                                    |
| tornado_http             | 136 ms                                                 | 139 ms: 1.02x slower                                                     |
| pycparser                | 1.58 sec                                               | 1.62 sec: 1.03x slower                                                   |
| richards_super           | 94.7 ms                                                | 97.2 ms: 1.03x slower                                                    |
| tomli_loads              | 3.14 sec                                               | 3.22 sec: 1.03x slower                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.69 ms: 1.03x slower                                                    |
| scimark_fft              | 466 ms                                                 | 483 ms: 1.04x slower                                                     |
| logging_silent           | 190 ns                                                 | 197 ns: 1.04x slower                                                     |
| json                     | 5.69 ms                                                | 5.93 ms: 1.04x slower                                                    |
| deepcopy_reduce          | 4.17 us                                                | 4.39 us: 1.05x slower                                                    |
| deltablue                | 7.91 ms                                                | 8.38 ms: 1.06x slower                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 125 ms: 1.06x slower                                                     |
| pyflate                  | 716 ms                                                 | 765 ms: 1.07x slower                                                     |
| spectral_norm            | 170 ms                                                 | 183 ms: 1.08x slower                                                     |
| chaos                    | 115 ms                                                 | 125 ms: 1.08x slower                                                     |
| nqueens                  | 106 ms                                                 | 117 ms: 1.10x slower                                                     |
| xml_etree_generate       | 99.4 ms                                                | 110 ms: 1.11x slower                                                     |
| html5lib                 | 88.9 ms                                                | 98.6 ms: 1.11x slower                                                    |
| sympy_integrate          | 25.8 ms                                                | 28.7 ms: 1.11x slower                                                    |
| xml_etree_process        | 79.1 ms                                                | 88.3 ms: 1.12x slower                                                    |
| mdp                      | 2.85 sec                                               | 3.19 sec: 1.12x slower                                                   |
| 2to3                     | 348 ms                                                 | 395 ms: 1.13x slower                                                     |
| fannkuch                 | 532 ms                                                 | 605 ms: 1.14x slower                                                     |
| thrift                   | 1.07 ms                                                | 1.23 ms: 1.15x slower                                                    |
| regex_compile            | 188 ms                                                 | 217 ms: 1.15x slower                                                     |
| hexiom                   | 10.4 ms                                                | 12.0 ms: 1.15x slower                                                    |
| meteor_contest           | 120 ms                                                 | 141 ms: 1.18x slower                                                     |
| pickle_pure_python       | 484 us                                                 | 575 us: 1.19x slower                                                     |
| raytrace                 | 507 ms                                                 | 603 ms: 1.19x slower                                                     |
| float                    | 117 ms                                                 | 139 ms: 1.19x slower                                                     |
| sqlglot_normalize        | 143 ms                                                 | 171 ms: 1.20x slower                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 3.10 ms: 1.20x slower                                                    |
| sqlglot_parse            | 2.17 ms                                                | 2.63 ms: 1.21x slower                                                    |
| sympy_str                | 346 ms                                                 | 422 ms: 1.22x slower                                                     |
| scimark_sor              | 220 ms                                                 | 268 ms: 1.22x slower                                                     |
| unpickle_pure_python     | 331 us                                                 | 408 us: 1.23x slower                                                     |
| django_template          | 48.2 ms                                                | 59.8 ms: 1.24x slower                                                    |
| genshi_xml               | 66.0 ms                                                | 82.4 ms: 1.25x slower                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 86.6 ms: 1.25x slower                                                    |
| genshi_text              | 31.8 ms                                                | 39.9 ms: 1.25x slower                                                    |
| async_generators         | 444 ms                                                 | 557 ms: 1.26x slower                                                     |
| logging_simple           | 8.30 us                                                | 10.4 us: 1.26x slower                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 1.28 sec: 1.26x slower                                                   |
| pprint_pformat           | 2.10 sec                                               | 2.66 sec: 1.27x slower                                                   |
| logging_format           | 9.09 us                                                | 11.7 us: 1.28x slower                                                    |
| go                       | 240 ms                                                 | 309 ms: 1.29x slower                                                     |
| mako                     | 16.3 ms                                                | 21.1 ms: 1.30x slower                                                    |
| sympy_sum                | 196 ms                                                 | 256 ms: 1.30x slower                                                     |
| sympy_expand             | 566 ms                                                 | 746 ms: 1.32x slower                                                     |
| scimark_lu               | 176 ms                                                 | 238 ms: 1.35x slower                                                     |
| telco                    | 7.27 ms                                                | 10.2 ms: 1.40x slower                                                    |
| nbody                    | 154 ms                                                 | 223 ms: 1.45x slower                                                     |
| coverage                 | 79.4 ms                                                | 116 ms: 1.46x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 9.30 ms: 1.57x slower                                                    |
| bench_thread_pool        | 986 us                                                 | 3.12 ms: 3.16x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.05x slower                                                             |

Benchmark hidden because not significant (1): comprehensions
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240813-3.14.0a0-4b27f3a-NOGIL/bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.28x