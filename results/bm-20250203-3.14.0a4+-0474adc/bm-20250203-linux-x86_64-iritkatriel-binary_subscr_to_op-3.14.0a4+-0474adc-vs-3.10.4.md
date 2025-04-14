# Results vs. 3.10.4

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: 0474adc
- commit date: 2025-02-03
- overall geometric mean: 1.457x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 252 ms: 1.38x faster                                                       |
| docutils       | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                     |
| html5lib       | 88.9 ms                                                | 61.2 ms: 1.45x faster                                                      |
| Geometric mean | (ref)                                                  | 1.37x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 616 ms: 2.87x faster                                                       |
| async_tree_none         | 728 ms                                                 | 264 ms: 2.76x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 321 ms: 2.71x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 487 ms: 2.09x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.1 ms: 1.67x faster                                                      |
| nbody          | 154 ms                                                 | 93.7 ms: 1.64x faster                                                      |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.41x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                       |
| regex_v8       | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.27 ms: 1.11x faster                                                      |
| regex_dna      | 227 ms                                                 | 209 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                  | 1.19x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.64x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.53x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                      |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.23x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 83.5 ms: 1.19x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 97.1 ms: 1.19x faster                                                      |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.8 ms: 1.51x faster                                                      |
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.49x faster                                                      |
| mako            | 16.3 ms                                                | 10.9 ms: 1.49x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 48.6 ms: 1.36x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 158 us: 3.43x faster                                                       |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 616 ms: 2.87x faster                                                       |
| async_tree_none          | 728 ms                                                 | 264 ms: 2.76x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 321 ms: 2.71x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 487 ms: 2.09x faster                                                       |
| go                       | 240 ms                                                 | 118 ms: 2.04x faster                                                       |
| pylint                   | 551 ms                                                 | 271 ms: 2.03x faster                                                       |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 30.1 us: 1.94x faster                                                      |
| deepcopy                 | 479 us                                                 | 253 us: 1.89x faster                                                       |
| richards_super           | 94.7 ms                                                | 50.6 ms: 1.87x faster                                                      |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 70.0 ms: 1.83x faster                                                      |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.81x faster                                                       |
| spectral_norm            | 170 ms                                                 | 94.6 ms: 1.80x faster                                                      |
| richards                 | 79.3 ms                                                | 44.4 ms: 1.79x faster                                                      |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                                       |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.77x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 68.3 ms: 1.73x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.72x faster                                                      |
| float                    | 117 ms                                                 | 70.1 ms: 1.67x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.24 ms: 1.67x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                      |
| nbody                    | 154 ms                                                 | 93.7 ms: 1.64x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.64x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                      |
| pyflate                  | 716 ms                                                 | 467 ms: 1.53x faster                                                       |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.53x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.47 us: 1.52x faster                                                      |
| django_template          | 48.2 ms                                                | 31.8 ms: 1.51x faster                                                      |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                       |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.49x faster                                                      |
| mako                     | 16.3 ms                                                | 10.9 ms: 1.49x faster                                                      |
| logging_format           | 9.09 us                                                | 6.10 us: 1.49x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                                      |
| html5lib                 | 88.9 ms                                                | 61.2 ms: 1.45x faster                                                      |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.3 ms: 1.43x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 719 ms: 1.42x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.59 ms: 1.41x faster                                                      |
| thrift                   | 1.07 ms                                                | 762 us: 1.41x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 103 ms: 1.39x faster                                                       |
| 2to3                     | 348 ms                                                 | 252 ms: 1.38x faster                                                       |
| scimark_fft              | 466 ms                                                 | 340 ms: 1.37x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 48.6 ms: 1.36x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.35x faster                                                       |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.35x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 51.7 ms: 1.34x faster                                                      |
| nqueens                  | 106 ms                                                 | 79.9 ms: 1.32x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 64.1 ms: 1.32x faster                                                      |
| sympy_str                | 346 ms                                                 | 265 ms: 1.31x faster                                                       |
| fannkuch                 | 532 ms                                                 | 408 ms: 1.30x faster                                                       |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                     |
| sympy_expand             | 566 ms                                                 | 449 ms: 1.26x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.23x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 83.5 ms: 1.19x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 97.1 ms: 1.19x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.45 sec: 1.16x faster                                                     |
| async_generators         | 444 ms                                                 | 382 ms: 1.16x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 860 us: 1.15x faster                                                       |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                      |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.27 ms: 1.11x faster                                                      |
| json                     | 5.69 ms                                                | 5.15 ms: 1.10x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.10x faster                                                      |
| regex_dna                | 227 ms                                                 | 209 ms: 1.08x faster                                                       |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                                      |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                       |
| telco                    | 7.27 ms                                                | 7.86 ms: 1.08x slower                                                      |
| coverage                 | 79.4 ms                                                | 89.9 ms: 1.13x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 5.03 ms: 1.39x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 81.0 ms: 3.37x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                               |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250203-3.14.0a4+-0474adc/bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.457x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.26x