# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: darwin-arm64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 176 ms: 1.09x faster                                                    |
| docutils       | 1.73 sec                                               | 1.57 sec: 1.11x faster                                                  |
| html5lib       | 42.4 ms                                                | 33.0 ms: 1.28x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 202 ms: 1.92x faster                                                    |
| async_tree_memoization  | 474 ms                                                 | 249 ms: 1.90x faster                                                    |
| async_tree_io           | 980 ms                                                 | 592 ms: 1.66x faster                                                    |
| async_tree_cpu_io_mixed | 649 ms                                                 | 462 ms: 1.41x faster                                                    |
| Geometric mean          | (ref)                                                  | 1.71x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 45.8 ms: 1.51x faster                                                   |
| nbody          | 93.0 ms                                                | 64.2 ms: 1.45x faster                                                   |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.30x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 76.0 ms: 1.25x faster                                                   |
| regex_dna      | 174 ms                                                 | 146 ms: 1.19x faster                                                    |
| regex_v8       | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.48 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 176 us: 1.59x faster                                                    |
| unpickle_pure_python | 194 us                                                 | 131 us: 1.49x faster                                                    |
| tomli_loads          | 1.71 sec                                               | 1.24 sec: 1.37x faster                                                  |
| xml_etree_process    | 46.5 ms                                                | 34.2 ms: 1.36x faster                                                   |
| json_dumps           | 8.11 ms                                                | 6.18 ms: 1.31x faster                                                   |
| xml_etree_generate   | 53.5 ms                                                | 50.5 ms: 1.06x faster                                                   |
| xml_etree_iterparse  | 72.1 ms                                                | 71.4 ms: 1.01x faster                                                   |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                                   |
| unpickle             | 8.80 us                                                | 9.18 us: 1.04x slower                                                   |
| pickle               | 6.97 us                                                | 7.44 us: 1.07x slower                                                   |
| unpickle_list        | 2.69 us                                                | 2.90 us: 1.08x slower                                                   |
| pickle_dict          | 17.0 us                                                | 18.3 us: 1.08x slower                                                   |
| pickle_list          | 2.74 us                                                | 2.99 us: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.8 ms: 1.55x slower                                                   |
| python_startup_no_site | 7.91 ms                                                | 13.7 ms: 1.73x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.63x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.43 ms: 1.53x faster                                                   |
| django_template | 26.4 ms                                                | 22.4 ms: 1.18x faster                                                   |
| genshi_text     | 17.3 ms                                                | 16.5 ms: 1.05x faster                                                   |
| genshi_xml      | 33.8 ms                                                | 41.2 ms: 1.22x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 93.6 us: 3.45x faster                                                   |
| deepcopy_memo            | 34.7 us                                                | 16.0 us: 2.17x faster                                                   |
| deltablue                | 4.91 ms                                                | 2.35 ms: 2.09x faster                                                   |
| async_tree_none          | 388 ms                                                 | 202 ms: 1.92x faster                                                    |
| async_tree_memoization   | 474 ms                                                 | 249 ms: 1.90x faster                                                    |
| logging_silent           | 117 ns                                                 | 63.0 ns: 1.86x faster                                                   |
| deepcopy                 | 272 us                                                 | 154 us: 1.77x faster                                                    |
| raytrace                 | 301 ms                                                 | 173 ms: 1.74x faster                                                    |
| async_tree_io            | 980 ms                                                 | 592 ms: 1.66x faster                                                    |
| chaos                    | 65.8 ms                                                | 40.1 ms: 1.64x faster                                                   |
| scimark_lu               | 103 ms                                                 | 63.2 ms: 1.63x faster                                                   |
| pickle_pure_python       | 281 us                                                 | 176 us: 1.59x faster                                                    |
| asyncio_tcp              | 659 ms                                                 | 424 ms: 1.55x faster                                                    |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.54x faster                                                   |
| mako                     | 9.87 ms                                                | 6.43 ms: 1.53x faster                                                   |
| float                    | 69.0 ms                                                | 45.8 ms: 1.51x faster                                                   |
| go                       | 151 ms                                                 | 101 ms: 1.50x faster                                                    |
| unpickle_pure_python     | 194 us                                                 | 131 us: 1.49x faster                                                    |
| logging_simple           | 4.45 us                                                | 3.01 us: 1.48x faster                                                   |
| logging_format           | 4.83 us                                                | 3.29 us: 1.47x faster                                                   |
| scimark_sor              | 128 ms                                                 | 87.4 ms: 1.47x faster                                                   |
| sqlglot_parse            | 1.24 ms                                                | 855 us: 1.45x faster                                                    |
| nbody                    | 93.0 ms                                                | 64.2 ms: 1.45x faster                                                   |
| spectral_norm            | 94.8 ms                                                | 66.7 ms: 1.42x faster                                                   |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 462 ms: 1.41x faster                                                    |
| sqlglot_transpile        | 1.44 ms                                                | 1.04 ms: 1.39x faster                                                   |
| crypto_pyaes             | 71.8 ms                                                | 52.0 ms: 1.38x faster                                                   |
| tomli_loads              | 1.71 sec                                               | 1.24 sec: 1.37x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 48.0 ms: 1.36x faster                                                   |
| xml_etree_process        | 46.5 ms                                                | 34.2 ms: 1.36x faster                                                   |
| thrift                   | 572 us                                                 | 424 us: 1.35x faster                                                    |
| pylint                   | 277 ms                                                 | 206 ms: 1.34x faster                                                    |
| generators               | 32.3 ms                                                | 24.4 ms: 1.33x faster                                                   |
| comprehensions           | 16.9 us                                                | 12.8 us: 1.32x faster                                                   |
| json_dumps               | 8.11 ms                                                | 6.18 ms: 1.31x faster                                                   |
| hexiom                   | 6.19 ms                                                | 4.75 ms: 1.30x faster                                                   |
| pyflate                  | 427 ms                                                 | 330 ms: 1.29x faster                                                    |
| html5lib                 | 42.4 ms                                                | 33.0 ms: 1.28x faster                                                   |
| pycparser                | 877 ms                                                 | 688 ms: 1.27x faster                                                    |
| pprint_safe_repr         | 641 ms                                                 | 509 ms: 1.26x faster                                                    |
| pprint_pformat           | 1.30 sec                                               | 1.04 sec: 1.26x faster                                                  |
| regex_compile            | 95.3 ms                                                | 76.0 ms: 1.25x faster                                                   |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.28 sec: 1.25x faster                                                  |
| coroutines               | 20.7 ms                                                | 16.6 ms: 1.25x faster                                                   |
| richards_super           | 57.8 ms                                                | 46.7 ms: 1.24x faster                                                   |
| scimark_fft              | 224 ms                                                 | 184 ms: 1.22x faster                                                    |
| dulwich_log              | 35.3 ms                                                | 29.1 ms: 1.22x faster                                                   |
| sympy_sum                | 92.2 ms                                                | 76.4 ms: 1.21x faster                                                   |
| regex_dna                | 174 ms                                                 | 146 ms: 1.19x faster                                                    |
| django_template          | 26.4 ms                                                | 22.4 ms: 1.18x faster                                                   |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.98 ms: 1.15x faster                                                   |
| sympy_str                | 165 ms                                                 | 144 ms: 1.15x faster                                                    |
| fannkuch                 | 303 ms                                                 | 266 ms: 1.14x faster                                                    |
| sympy_integrate          | 13.1 ms                                                | 11.7 ms: 1.12x faster                                                   |
| bench_thread_pool        | 527 us                                                 | 474 us: 1.11x faster                                                    |
| mdp                      | 1.63 sec                                               | 1.47 sec: 1.11x faster                                                  |
| nqueens                  | 63.8 ms                                                | 57.7 ms: 1.11x faster                                                   |
| docutils                 | 1.73 sec                                               | 1.57 sec: 1.11x faster                                                  |
| richards                 | 48.7 ms                                                | 44.6 ms: 1.09x faster                                                   |
| 2to3                     | 192 ms                                                 | 176 ms: 1.09x faster                                                    |
| sympy_expand             | 269 ms                                                 | 248 ms: 1.09x faster                                                    |
| xml_etree_generate       | 53.5 ms                                                | 50.5 ms: 1.06x faster                                                   |
| json                     | 3.08 ms                                                | 2.92 ms: 1.05x faster                                                   |
| genshi_text              | 17.3 ms                                                | 16.5 ms: 1.05x faster                                                   |
| pathlib                  | 24.5 ms                                                | 23.3 ms: 1.05x faster                                                   |
| meteor_contest           | 77.7 ms                                                | 74.4 ms: 1.05x faster                                                   |
| sqlglot_normalize        | 190 ms                                                 | 182 ms: 1.04x faster                                                    |
| sqlglot_optimize         | 36.8 ms                                                | 35.4 ms: 1.04x faster                                                   |
| regex_v8                 | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                   |
| xml_etree_iterparse      | 72.1 ms                                                | 71.4 ms: 1.01x faster                                                   |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                    |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                    |
| regex_effbot             | 2.46 ms                                                | 2.48 ms: 1.01x slower                                                   |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                                   |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                   |
| unpickle                 | 8.80 us                                                | 9.18 us: 1.04x slower                                                   |
| create_gc_cycles         | 860 us                                                 | 898 us: 1.04x slower                                                    |
| pickle                   | 6.97 us                                                | 7.44 us: 1.07x slower                                                   |
| sqlite_synth             | 1.46 us                                                | 1.57 us: 1.08x slower                                                   |
| coverage                 | 41.5 ms                                                | 44.7 ms: 1.08x slower                                                   |
| unpickle_list            | 2.69 us                                                | 2.90 us: 1.08x slower                                                   |
| pickle_dict              | 17.0 us                                                | 18.3 us: 1.08x slower                                                   |
| pickle_list              | 2.74 us                                                | 2.99 us: 1.09x slower                                                   |
| genshi_xml               | 33.8 ms                                                | 41.2 ms: 1.22x slower                                                   |
| async_generators         | 231 ms                                                 | 292 ms: 1.26x slower                                                    |
| telco                    | 3.49 ms                                                | 4.65 ms: 1.33x slower                                                   |
| bench_mp_pool            | 37.4 ms                                                | 51.5 ms: 1.38x slower                                                   |
| python_startup           | 10.9 ms                                                | 16.8 ms: 1.55x slower                                                   |
| python_startup_no_site   | 7.91 ms                                                | 13.7 ms: 1.73x slower                                                   |
| unpack_sequence          | 39.0 ns                                                | 76.3 ns: 1.95x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.21x faster                                                            |

Benchmark hidden because not significant (2): xml_etree_parse, tornado_http
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 0.99x