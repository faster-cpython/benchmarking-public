# Results vs. 3.10.4

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.162x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| docutils       | 1.92 sec                                                    | 2.74 sec: 1.43x slower                                                     |
| html5lib       | 51.0 ms                                                     | 41.5 ms: 1.23x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 346 ms: 3.20x faster                                                       |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.55x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 209 ms: 2.52x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 325 ms: 1.96x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.52x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.9 ms: 1.34x faster                                                      |
| pidigits       | 149 ms                                                      | 134 ms: 1.11x faster                                                       |
| nbody          | 71.3 ms                                                     | 80.1 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.20x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                      |
| regex_compile  | 106 ms                                                      | 94.1 ms: 1.13x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.94 ms: 1.54x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 157 us: 1.17x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 232 us: 1.16x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 57.2 ms: 1.14x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 89.5 ms: 1.08x faster                                                      |
| pickle_list          | 2.75 us                                                     | 2.99 us: 1.09x slower                                                      |
| unpickle             | 9.09 us                                                     | 10.2 us: 1.12x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 62.3 ms: 1.12x slower                                                      |
| json_loads           | 14.0 us                                                     | 15.9 us: 1.13x slower                                                      |
| pickle               | 6.85 us                                                     | 7.82 us: 1.14x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.13 us: 1.15x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.8 us: 1.15x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.60 sec: 1.56x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.4 ms: 1.24x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 27.2 ms: 1.06x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 40.0 ms: 1.03x faster                                                      |
| mako            | 9.03 ms                                                     | 10.1 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 346 ms: 3.20x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 131 us: 2.56x faster                                                       |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.55x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.7 ms: 2.55x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 209 ms: 2.52x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 325 ms: 1.96x faster                                                       |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.44 ms: 1.71x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 439 ms: 1.67x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.08 sec: 1.65x faster                                                     |
| logging_silent           | 94.6 ns                                                     | 61.2 ns: 1.55x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.94 ms: 1.54x faster                                                      |
| go                       | 139 ms                                                      | 91.3 ms: 1.52x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.34 us: 1.42x faster                                                      |
| generators               | 32.4 ms                                                     | 23.2 ms: 1.40x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.2 us: 1.35x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 21.4 us: 1.34x faster                                                      |
| float                    | 61.7 ms                                                     | 45.9 ms: 1.34x faster                                                      |
| chaos                    | 61.7 ms                                                     | 46.5 ms: 1.33x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 65.0 ms: 1.32x faster                                                      |
| pyflate                  | 409 ms                                                      | 311 ms: 1.31x faster                                                       |
| raytrace                 | 273 ms                                                      | 208 ms: 1.31x faster                                                       |
| pycparser                | 930 ms                                                      | 720 ms: 1.29x faster                                                       |
| richards_super           | 52.2 ms                                                     | 41.1 ms: 1.27x faster                                                      |
| deepcopy                 | 255 us                                                      | 205 us: 1.24x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.8 ms: 1.24x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.67 ms: 1.23x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 41.5 ms: 1.23x faster                                                      |
| scimark_sor              | 106 ms                                                      | 86.6 ms: 1.23x faster                                                      |
| richards                 | 42.4 ms                                                     | 35.4 ms: 1.20x faster                                                      |
| regex_dna                | 136 ms                                                      | 114 ms: 1.20x faster                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.19 ms: 1.19x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 157 us: 1.17x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 232 us: 1.16x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 57.2 ms: 1.14x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.8 ms: 1.13x faster                                                      |
| regex_compile            | 106 ms                                                      | 94.1 ms: 1.13x faster                                                      |
| sympy_sum                | 107 ms                                                      | 95.2 ms: 1.12x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 55.7 ms: 1.12x faster                                                      |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| pidigits                 | 149 ms                                                      | 134 ms: 1.11x faster                                                       |
| thrift                   | 617 us                                                      | 556 us: 1.11x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.8 ms: 1.11x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.10x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 71.1 ms: 1.09x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 89.5 ms: 1.08x faster                                                      |
| django_template          | 28.9 ms                                                     | 27.2 ms: 1.06x faster                                                      |
| sympy_str                | 194 ms                                                      | 185 ms: 1.05x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 38.0 ns: 1.04x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 573 ms: 1.03x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 40.0 ms: 1.03x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.16 us: 1.02x faster                                                      |
| json                     | 3.14 ms                                                     | 3.08 ms: 1.02x faster                                                      |
| logging_format           | 6.76 us                                                     | 7.09 us: 1.05x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.67 us: 1.07x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 71.6 ms: 1.08x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.99 us: 1.09x slower                                                      |
| mako                     | 9.03 ms                                                     | 10.1 ms: 1.11x slower                                                      |
| unpickle                 | 9.09 us                                                     | 10.2 us: 1.12x slower                                                      |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                                       |
| bench_thread_pool        | 958 us                                                      | 1.07 ms: 1.12x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 62.3 ms: 1.12x slower                                                      |
| nbody                    | 71.3 ms                                                     | 80.1 ms: 1.12x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 85.5 ms: 1.13x slower                                                      |
| json_loads               | 14.0 us                                                     | 15.9 us: 1.13x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.09 ms: 1.14x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.82 us: 1.14x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.13 us: 1.15x slower                                                      |
| scimark_fft              | 187 ms                                                      | 216 ms: 1.15x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 19.8 us: 1.15x slower                                                      |
| fannkuch                 | 256 ms                                                      | 302 ms: 1.18x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.76 ms: 1.21x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.4 ms: 1.24x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 995 us: 1.24x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 77.6 ms: 1.25x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.69 sec: 1.39x slower                                                     |
| docutils                 | 1.92 sec                                                    | 2.74 sec: 1.43x slower                                                     |
| tomli_loads              | 1.67 sec                                                    | 2.60 sec: 1.56x slower                                                     |
| coverage                 | 39.0 ms                                                     | 67.3 ms: 1.72x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (4): asyncio_tcp_ssl, genshi_text, sympy_expand, xml_etree_process
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250823-3.15.0a0-6fcac09-NOGIL/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.162x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown