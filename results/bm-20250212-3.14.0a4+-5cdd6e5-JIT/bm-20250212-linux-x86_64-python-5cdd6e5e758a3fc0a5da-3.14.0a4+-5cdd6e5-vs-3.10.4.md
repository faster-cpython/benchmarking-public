# Results vs. 3.10.4

- fork: python
- ref: 5cdd6e5e758a3fc0a5da
- machine: linux-x86_64
- commit hash: 5cdd6e5
- commit date: 2025-02-12
- overall geometric mean: 1.447x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                   |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                 |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                  |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 625 ms: 2.83x faster                                                   |
| async_tree_none         | 728 ms                                                 | 268 ms: 2.72x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 328 ms: 2.65x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.55x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.5 ms: 1.66x faster                                                  |
| nbody          | 154 ms                                                 | 93.5 ms: 1.64x faster                                                  |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.40x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                                   |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.16 ms: 1.15x faster                                                  |
| regex_dna      | 227 ms                                                 | 207 ms: 1.10x faster                                                   |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.84 sec: 1.71x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 199 us: 1.66x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 55.5 ms: 1.43x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 78.3 ms: 1.27x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 96.2 ms: 1.20x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.9 ms: 1.19x faster                                                  |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                  |
| django_template | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                  |
| genshi_text     | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.4 ms: 1.34x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.48x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                   |
| generators               | 80.1 ms                                                | 27.7 ms: 2.89x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 625 ms: 2.83x faster                                                   |
| async_tree_none          | 728 ms                                                 | 268 ms: 2.72x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 328 ms: 2.65x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.37 ms: 2.35x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                                   |
| chaos                    | 115 ms                                                 | 58.4 ms: 1.98x faster                                                  |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 30.7 us: 1.91x faster                                                  |
| richards_super           | 94.7 ms                                                | 49.8 ms: 1.90x faster                                                  |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                   |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                   |
| go                       | 240 ms                                                 | 131 ms: 1.84x faster                                                   |
| richards                 | 79.3 ms                                                | 43.4 ms: 1.83x faster                                                  |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.82x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 70.7 ms: 1.81x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 65.8 ms: 1.80x faster                                                  |
| logging_silent           | 190 ns                                                 | 106 ns: 1.80x faster                                                   |
| spectral_norm            | 170 ms                                                 | 95.7 ms: 1.78x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.84 sec: 1.71x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 199 us: 1.66x faster                                                   |
| float                    | 117 ms                                                 | 70.5 ms: 1.66x faster                                                  |
| nbody                    | 154 ms                                                 | 93.5 ms: 1.64x faster                                                  |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                  |
| pyflate                  | 716 ms                                                 | 457 ms: 1.57x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                   |
| django_template          | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                  |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.93 ms: 1.50x faster                                                  |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                                   |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                  |
| logging_format           | 9.09 us                                                | 6.12 us: 1.48x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.48 ms: 1.44x faster                                                  |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.10 sec: 1.43x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 55.5 ms: 1.43x faster                                                  |
| thrift                   | 1.07 ms                                                | 763 us: 1.40x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 751 ms: 1.35x faster                                                   |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.35x faster                                                   |
| fannkuch                 | 532 ms                                                 | 395 ms: 1.35x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 49.4 ms: 1.34x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                   |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 53.6 ms: 1.29x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.2 ms: 1.28x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 66.1 ms: 1.28x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 78.3 ms: 1.27x faster                                                  |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                                   |
| sympy_expand             | 566 ms                                                 | 470 ms: 1.20x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 96.2 ms: 1.20x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.9 ms: 1.19x faster                                                  |
| nqueens                  | 106 ms                                                 | 89.3 ms: 1.19x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.16 ms: 1.15x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 889 us: 1.11x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                 |
| json                     | 5.69 ms                                                | 5.14 ms: 1.11x faster                                                  |
| regex_dna                | 227 ms                                                 | 207 ms: 1.10x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                  |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                                  |
| async_generators         | 444 ms                                                 | 413 ms: 1.07x faster                                                   |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                   |
| telco                    | 7.27 ms                                                | 7.59 ms: 1.05x slower                                                  |
| coverage                 | 79.4 ms                                                | 89.8 ms: 1.13x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.95 ms: 1.37x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                           |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250212-3.14.0a4+-5cdd6e5-JIT/bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.447x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x