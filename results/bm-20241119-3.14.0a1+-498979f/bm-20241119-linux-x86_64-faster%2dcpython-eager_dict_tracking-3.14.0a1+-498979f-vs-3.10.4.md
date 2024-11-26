# Results vs. 3.10.4

- fork: faster-cpython
- ref: eager_dict_tracking
- machine: linux-x86_64
- commit hash: 498979f
- commit date: 2024-11-19
- overall geometric mean: 1.409x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                                            |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                          |
| html5lib       | 88.9 ms                                                | 64.0 ms: 1.39x faster                                                           |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 321 ms: 2.27x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 403 ms: 2.16x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 906 ms: 1.95x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 559 ms: 1.82x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 92.9 ms: 1.65x faster                                                           |
| float          | 117 ms                                                 | 81.6 ms: 1.44x faster                                                           |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                            |
| regex_v8       | 27.8 ms                                                | 26.3 ms: 1.06x faster                                                           |
| regex_effbot   | 3.63 ms                                                | 3.48 ms: 1.04x faster                                                           |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                            |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.12 sec: 1.48x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                           |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                           |
| json_loads           | 31.2 us                                                | 26.6 us: 1.17x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 86.0 ms: 1.16x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 151 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                           |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                           |
| genshi_text     | 31.8 ms                                                | 22.3 ms: 1.42x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.33x faster                                                            |
| generators               | 80.1 ms                                                | 27.6 ms: 2.90x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.38 ms: 2.34x faster                                                           |
| async_tree_none          | 728 ms                                                 | 321 ms: 2.27x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 403 ms: 2.16x faster                                                            |
| pylint                   | 551 ms                                                 | 262 ms: 2.10x faster                                                            |
| go                       | 240 ms                                                 | 123 ms: 1.96x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 906 ms: 1.95x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 30.8 us: 1.90x faster                                                           |
| chaos                    | 115 ms                                                 | 61.1 ms: 1.89x faster                                                           |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                            |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 559 ms: 1.82x faster                                                            |
| richards_super           | 94.7 ms                                                | 53.6 ms: 1.77x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 73.6 ms: 1.74x faster                                                           |
| logging_silent           | 190 ns                                                 | 110 ns: 1.73x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 68.8 ms: 1.72x faster                                                           |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.71x faster                                                            |
| djangocms                | 38.4 us                                                | 22.5 us: 1.71x faster                                                           |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.22 ms: 1.67x faster                                                           |
| richards                 | 79.3 ms                                                | 47.6 ms: 1.66x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                           |
| nbody                    | 154 ms                                                 | 92.9 ms: 1.65x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.60x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                           |
| pyflate                  | 716 ms                                                 | 469 ms: 1.53x faster                                                            |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.50x faster                                                           |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.50x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                            |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                           |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.12 sec: 1.48x faster                                                          |
| logging_format           | 9.09 us                                                | 6.17 us: 1.47x faster                                                           |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                            |
| float                    | 117 ms                                                 | 81.6 ms: 1.44x faster                                                           |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                           |
| genshi_text              | 31.8 ms                                                | 22.3 ms: 1.42x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 729 ms: 1.40x faster                                                            |
| thrift                   | 1.07 ms                                                | 770 us: 1.39x faster                                                            |
| html5lib                 | 88.9 ms                                                | 64.0 ms: 1.39x faster                                                           |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.76 ms: 1.36x faster                                                           |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                                            |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.35x faster                                                            |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                           |
| nqueens                  | 106 ms                                                 | 80.0 ms: 1.32x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                           |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 64.9 ms: 1.30x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 53.3 ms: 1.30x faster                                                           |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                            |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.28x faster                                                           |
| scimark_fft              | 466 ms                                                 | 365 ms: 1.28x faster                                                            |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                           |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                          |
| json_loads               | 31.2 us                                                | 26.6 us: 1.17x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 851 us: 1.16x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 86.0 ms: 1.16x faster                                                           |
| json                     | 5.69 ms                                                | 4.96 ms: 1.15x faster                                                           |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                           |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 151 ms: 1.11x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.68 sec: 1.06x faster                                                          |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 26.3 ms: 1.06x faster                                                           |
| regex_effbot             | 3.63 ms                                                | 3.48 ms: 1.04x faster                                                           |
| async_generators         | 444 ms                                                 | 430 ms: 1.03x faster                                                            |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                            |
| coverage                 | 79.4 ms                                                | 85.5 ms: 1.08x slower                                                           |
| telco                    | 7.27 ms                                                | 7.94 ms: 1.09x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 4.31 ms: 1.19x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.64 ms: 1.63x slower                                                           |
| bench_mp_pool            | 24.0 ms                                                | 78.5 ms: 3.27x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                                    |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241119-3.14.0a1+-498979f/bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.409x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.25x