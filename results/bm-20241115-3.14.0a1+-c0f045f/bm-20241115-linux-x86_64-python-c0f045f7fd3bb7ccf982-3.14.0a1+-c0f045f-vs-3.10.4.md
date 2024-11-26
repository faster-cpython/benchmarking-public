# Results vs. 3.10.4

- fork: python
- ref: c0f045f7fd3bb7ccf982
- machine: linux-x86_64
- commit hash: c0f045f
- commit date: 2024-11-15
- overall geometric mean: 1.401x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                   |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                 |
| html5lib       | 88.9 ms                                                | 65.5 ms: 1.36x faster                                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 330 ms: 2.20x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 414 ms: 2.10x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 855 ms: 2.07x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 571 ms: 1.78x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 97.2 ms: 1.58x faster                                                  |
| float          | 117 ms                                                 | 80.2 ms: 1.46x faster                                                  |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.33x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                   |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                  |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.83 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 329 us: 1.47x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                  |
| json_loads           | 31.2 us                                                | 26.8 us: 1.16x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 159 ms: 1.06x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                  |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                  |
| genshi_text     | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 50.4 ms: 1.31x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.38x faster                                                   |
| generators               | 80.1 ms                                                | 28.8 ms: 2.78x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.37 ms: 2.35x faster                                                  |
| async_tree_none          | 728 ms                                                 | 330 ms: 2.20x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 414 ms: 2.10x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 855 ms: 2.07x faster                                                   |
| go                       | 240 ms                                                 | 123 ms: 1.95x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.92x faster                                                  |
| chaos                    | 115 ms                                                 | 61.4 ms: 1.88x faster                                                  |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                   |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                   |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                                   |
| richards_super           | 94.7 ms                                                | 53.1 ms: 1.78x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 571 ms: 1.78x faster                                                   |
| djangocms                | 38.4 us                                                | 22.1 us: 1.74x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 73.8 ms: 1.73x faster                                                  |
| pylint                   | 551 ms                                                 | 319 ms: 1.73x faster                                                   |
| richards                 | 79.3 ms                                                | 46.3 ms: 1.71x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 69.3 ms: 1.71x faster                                                  |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                   |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.66x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.35 ms: 1.64x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                  |
| nbody                    | 154 ms                                                 | 97.2 ms: 1.58x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                  |
| pyflate                  | 716 ms                                                 | 467 ms: 1.53x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                   |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                 |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.50x faster                                                  |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 329 us: 1.47x faster                                                   |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                                  |
| coroutines               | 35.1 ms                                                | 24.0 ms: 1.46x faster                                                  |
| float                    | 117 ms                                                 | 80.2 ms: 1.46x faster                                                  |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                   |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                  |
| genshi_text              | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                                   |
| thrift                   | 1.07 ms                                                | 776 us: 1.38x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                                  |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                   |
| html5lib                 | 88.9 ms                                                | 65.5 ms: 1.36x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.34x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                   |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                   |
| nqueens                  | 106 ms                                                 | 79.8 ms: 1.33x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 50.4 ms: 1.31x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 53.4 ms: 1.30x faster                                                  |
| fannkuch                 | 532 ms                                                 | 410 ms: 1.30x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.00 ms: 1.29x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                                  |
| scimark_fft              | 466 ms                                                 | 363 ms: 1.28x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                  |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 65.8 ms: 1.28x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                  |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                 |
| json_loads               | 31.2 us                                                | 26.8 us: 1.16x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 853 us: 1.16x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                  |
| json                     | 5.69 ms                                                | 4.99 ms: 1.14x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.06x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.68 sec: 1.06x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 159 ms: 1.06x faster                                                   |
| async_generators         | 444 ms                                                 | 429 ms: 1.03x faster                                                   |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.83 ms: 1.05x slower                                                  |
| coverage                 | 79.4 ms                                                | 84.6 ms: 1.06x slower                                                  |
| telco                    | 7.27 ms                                                | 7.81 ms: 1.07x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.61 ms: 1.27x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.70 ms: 1.67x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 78.4 ms: 3.26x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241115-3.14.0a1+-c0f045f/bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.401x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.26x