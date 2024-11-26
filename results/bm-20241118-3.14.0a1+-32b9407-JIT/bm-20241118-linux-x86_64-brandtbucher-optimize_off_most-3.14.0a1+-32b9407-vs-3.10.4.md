# Results vs. 3.10.4

- fork: brandtbucher
- ref: optimize_off_most
- machine: linux-x86_64
- commit hash: 32b9407
- commit date: 2024-11-18
- overall geometric mean: 1.299x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 300 ms: 1.16x faster                                                      |
| docutils       | 3.30 sec                                               | 3.27 sec: 1.01x faster                                                    |
| html5lib       | 88.9 ms                                                | 69.7 ms: 1.27x faster                                                     |
| Geometric mean | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 342 ms: 2.13x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 429 ms: 2.03x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 882 ms: 2.01x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 590 ms: 1.72x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.96x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 98.9 ms: 1.55x faster                                                     |
| float          | 117 ms                                                 | 80.7 ms: 1.45x faster                                                     |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.32x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 156 ms: 1.21x faster                                                      |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                     |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.80 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 228 us: 1.45x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 342 us: 1.42x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 60.8 ms: 1.30x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 83.6 ms: 1.19x faster                                                     |
| json_loads           | 31.2 us                                                | 26.4 us: 1.18x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                     |
| django_template | 48.2 ms                                                | 35.4 ms: 1.36x faster                                                     |
| genshi_text     | 31.8 ms                                                | 27.2 ms: 1.17x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 67.6 ms: 1.02x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.23x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 174 us: 3.13x faster                                                      |
| async_tree_none          | 728 ms                                                 | 342 ms: 2.13x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.73 ms: 2.12x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 429 ms: 2.03x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 882 ms: 2.01x faster                                                      |
| generators               | 80.1 ms                                                | 41.0 ms: 1.95x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 32.3 us: 1.81x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 73.3 ms: 1.74x faster                                                     |
| chaos                    | 115 ms                                                 | 66.7 ms: 1.73x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 590 ms: 1.72x faster                                                      |
| logging_silent           | 190 ns                                                 | 112 ns: 1.69x faster                                                      |
| raytrace                 | 507 ms                                                 | 304 ms: 1.67x faster                                                      |
| richards_super           | 94.7 ms                                                | 57.7 ms: 1.64x faster                                                     |
| richards                 | 79.3 ms                                                | 48.8 ms: 1.62x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 72.9 ms: 1.62x faster                                                     |
| deepcopy                 | 479 us                                                 | 298 us: 1.61x faster                                                      |
| djangocms                | 38.4 us                                                | 24.1 us: 1.59x faster                                                     |
| scimark_sor              | 220 ms                                                 | 138 ms: 1.59x faster                                                      |
| go                       | 240 ms                                                 | 151 ms: 1.59x faster                                                      |
| nbody                    | 154 ms                                                 | 98.9 ms: 1.55x faster                                                     |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                    |
| comprehensions           | 28.8 us                                                | 19.4 us: 1.48x faster                                                     |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.47 ms: 1.48x faster                                                     |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                     |
| float                    | 117 ms                                                 | 80.7 ms: 1.45x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 228 us: 1.45x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.92 us: 1.43x faster                                                     |
| pyflate                  | 716 ms                                                 | 505 ms: 1.42x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.85 us: 1.42x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 342 us: 1.42x faster                                                      |
| logging_format           | 9.09 us                                                | 6.47 us: 1.40x faster                                                     |
| pylint                   | 551 ms                                                 | 395 ms: 1.40x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.89 ms: 1.36x faster                                                     |
| django_template          | 48.2 ms                                                | 35.4 ms: 1.36x faster                                                     |
| thrift                   | 1.07 ms                                                | 792 us: 1.35x faster                                                      |
| spectral_norm            | 170 ms                                                 | 127 ms: 1.34x faster                                                      |
| scimark_fft              | 466 ms                                                 | 349 ms: 1.33x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 60.8 ms: 1.30x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.00 ms: 1.29x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 18.2 ms: 1.28x faster                                                     |
| html5lib                 | 88.9 ms                                                | 69.7 ms: 1.27x faster                                                     |
| hexiom                   | 10.4 ms                                                | 8.25 ms: 1.26x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.28 sec: 1.23x faster                                                    |
| fannkuch                 | 532 ms                                                 | 437 ms: 1.22x faster                                                      |
| regex_compile            | 188 ms                                                 | 156 ms: 1.21x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 70.8 ms: 1.19x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 83.6 ms: 1.19x faster                                                     |
| json_loads               | 31.2 us                                                | 26.4 us: 1.18x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 122 ms: 1.17x faster                                                      |
| genshi_text              | 31.8 ms                                                | 27.2 ms: 1.17x faster                                                     |
| json                     | 5.69 ms                                                | 4.90 ms: 1.16x faster                                                     |
| 2to3                     | 348 ms                                                 | 300 ms: 1.16x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 152 ms: 1.13x faster                                                      |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                     |
| nqueens                  | 106 ms                                                 | 94.2 ms: 1.12x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 910 ms: 1.12x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.89 sec: 1.11x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 915 us: 1.08x faster                                                      |
| sympy_str                | 346 ms                                                 | 323 ms: 1.07x faster                                                      |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.07x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 64.7 ms: 1.07x faster                                                     |
| sympy_expand             | 566 ms                                                 | 530 ms: 1.07x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.07x faster                                                     |
| sympy_sum                | 196 ms                                                 | 188 ms: 1.05x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 25.1 ms: 1.03x faster                                                     |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.80 sec: 1.02x faster                                                    |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                      |
| docutils                 | 3.30 sec                                               | 3.27 sec: 1.01x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.00x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 67.6 ms: 1.02x slower                                                     |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                                      |
| regex_effbot             | 3.63 ms                                                | 3.80 ms: 1.05x slower                                                     |
| telco                    | 7.27 ms                                                | 7.64 ms: 1.05x slower                                                     |
| coverage                 | 79.4 ms                                                | 84.4 ms: 1.06x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.36 ms: 1.20x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.68 ms: 1.65x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 86.6 ms: 3.61x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                              |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241118-3.14.0a1+-32b9407-JIT/bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.299x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.36x