# Results vs. base

- fork: brandtbucher
- ref: jump_backoff
- machine: linux-x86_64
- commit hash: 5dd5806
- commit date: 2024-11-13
- overall geometric mean: 1.012x faster
- HPT reliability: 98.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241113-linux-x86_64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                 | 262 ms: 1.07x faster                                                 |
| docutils       | 2.94 sec                                                               | 2.91 sec: 1.01x faster                                               |
| html5lib       | 66.7 ms                                                                | 67.2 ms: 1.01x slower                                                |
| sphinx         | 1.18 sec                                                               | 1.15 sec: 1.03x faster                                               |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20241113-linux-x86_64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|--------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| asyncio_websockets | 557 ms                                                                 | 553 ms: 1.01x faster                                                 |
| async_tree_io_tg   | 963 ms                                                                 | 987 ms: 1.02x slower                                                 |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (9): async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_generators, async_tree_none_tg, coroutines, async_tree_memoization_tg, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241113-linux-x86_64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 84.6 ms                                                                | 83.8 ms: 1.01x faster                                                |
| float          | 76.5 ms                                                                | 76.2 ms: 1.00x faster                                                |
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241113-linux-x86_64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 138 ms                                                                 | 134 ms: 1.03x faster                                                 |
| regex_v8       | 25.3 ms                                                                | 24.8 ms: 1.02x faster                                                |
| regex_effbot   | 3.79 ms                                                                | 3.83 ms: 1.01x slower                                                |
| regex_dna      | 219 ms                                                                 | 224 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241113-linux-x86_64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 219 us                                                                 | 195 us: 1.12x faster                                                 |
| tomli_loads          | 1.98 sec                                                               | 1.95 sec: 1.02x faster                                               |
| json_loads           | 26.7 us                                                                | 26.3 us: 1.01x faster                                                |
| xml_etree_iterparse  | 100 ms                                                                 | 102 ms: 1.02x slower                                                 |
| xml_etree_generate   | 79.3 ms                                                                | 82.8 ms: 1.04x slower                                                |
| xml_etree_parse      | 148 ms                                                                 | 155 ms: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (3): xml_etree_process, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241113-linux-x86_64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.12 ms                                                                | 7.04 ms: 1.01x faster                                                |
| python_startup         | 12.7 ms                                                                | 12.7 ms: 1.01x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241113-linux-x86_64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako           | 10.3 ms                                                                | 10.2 ms: 1.01x faster                                                |
| genshi_text    | 24.8 ms                                                                | 25.6 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20241113-linux-x86_64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-linux-x86_64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| richards_super           | 48.1 ms                                                                | 41.9 ms: 1.15x faster                                                |
| unpickle_pure_python     | 219 us                                                                 | 195 us: 1.12x faster                                                 |
| sympy_integrate          | 23.5 ms                                                                | 21.0 ms: 1.12x faster                                                |
| sqlalchemy_declarative   | 147 ms                                                                 | 132 ms: 1.11x faster                                                 |
| pylint                   | 378 ms                                                                 | 342 ms: 1.11x faster                                                 |
| gc_traversal             | 4.80 ms                                                                | 4.34 ms: 1.11x faster                                                |
| richards                 | 41.0 ms                                                                | 37.5 ms: 1.09x faster                                                |
| sympy_sum                | 176 ms                                                                 | 161 ms: 1.09x faster                                                 |
| sqlglot_optimize         | 60.6 ms                                                                | 55.7 ms: 1.09x faster                                                |
| bench_mp_pool            | 84.8 ms                                                                | 78.7 ms: 1.08x faster                                                |
| 2to3                     | 281 ms                                                                 | 262 ms: 1.07x faster                                                 |
| pycparser                | 1.21 sec                                                               | 1.14 sec: 1.06x faster                                               |
| logging_silent           | 99.8 ns                                                                | 95.5 ns: 1.04x faster                                                |
| sqlglot_normalize        | 116 ms                                                                 | 111 ms: 1.04x faster                                                 |
| fannkuch                 | 399 ms                                                                 | 385 ms: 1.04x faster                                                 |
| regex_compile            | 138 ms                                                                 | 134 ms: 1.03x faster                                                 |
| sqlglot_transpile        | 1.69 ms                                                                | 1.64 ms: 1.03x faster                                                |
| sympy_str                | 304 ms                                                                 | 295 ms: 1.03x faster                                                 |
| sphinx                   | 1.18 sec                                                               | 1.15 sec: 1.03x faster                                               |
| pprint_safe_repr         | 737 ms                                                                 | 719 ms: 1.03x faster                                                 |
| regex_v8                 | 25.3 ms                                                                | 24.8 ms: 1.02x faster                                                |
| bench_thread_pool        | 893 us                                                                 | 877 us: 1.02x faster                                                 |
| sqlalchemy_imperative    | 17.8 ms                                                                | 17.5 ms: 1.02x faster                                                |
| tomli_loads              | 1.98 sec                                                               | 1.95 sec: 1.02x faster                                               |
| json_loads               | 26.7 us                                                                | 26.3 us: 1.01x faster                                                |
| create_gc_cycles         | 2.70 ms                                                                | 2.66 ms: 1.01x faster                                                |
| deepcopy                 | 273 us                                                                 | 269 us: 1.01x faster                                                 |
| telco                    | 7.57 ms                                                                | 7.48 ms: 1.01x faster                                                |
| python_startup_no_site   | 7.12 ms                                                                | 7.04 ms: 1.01x faster                                                |
| docutils                 | 2.94 sec                                                               | 2.91 sec: 1.01x faster                                               |
| deltablue                | 3.31 ms                                                                | 3.27 ms: 1.01x faster                                                |
| nbody                    | 84.6 ms                                                                | 83.8 ms: 1.01x faster                                                |
| pprint_pformat           | 1.48 sec                                                               | 1.47 sec: 1.01x faster                                               |
| mako                     | 10.3 ms                                                                | 10.2 ms: 1.01x faster                                                |
| spectral_norm            | 116 ms                                                                 | 115 ms: 1.01x faster                                                 |
| sqlite_synth             | 2.82 us                                                                | 2.80 us: 1.01x faster                                                |
| python_startup           | 12.7 ms                                                                | 12.7 ms: 1.01x faster                                                |
| asyncio_websockets       | 557 ms                                                                 | 553 ms: 1.01x faster                                                 |
| go                       | 134 ms                                                                 | 134 ms: 1.01x faster                                                 |
| float                    | 76.5 ms                                                                | 76.2 ms: 1.00x faster                                                |
| meteor_contest           | 108 ms                                                                 | 107 ms: 1.00x faster                                                 |
| pidigits                 | 187 ms                                                                 | 186 ms: 1.00x faster                                                 |
| thrift                   | 777 us                                                                 | 782 us: 1.01x slower                                                 |
| nqueens                  | 87.1 ms                                                                | 87.7 ms: 1.01x slower                                                |
| hexiom                   | 7.10 ms                                                                | 7.15 ms: 1.01x slower                                                |
| html5lib                 | 66.7 ms                                                                | 67.2 ms: 1.01x slower                                                |
| regex_effbot             | 3.79 ms                                                                | 3.83 ms: 1.01x slower                                                |
| typing_runtime_protocols | 168 us                                                                 | 170 us: 1.01x slower                                                 |
| shortest_path            | 480 ms                                                                 | 485 ms: 1.01x slower                                                 |
| comprehensions           | 17.5 us                                                                | 17.7 us: 1.01x slower                                                |
| scimark_fft              | 318 ms                                                                 | 322 ms: 1.01x slower                                                 |
| k_core                   | 3.58 sec                                                               | 3.64 sec: 1.02x slower                                               |
| xml_etree_iterparse      | 100 ms                                                                 | 102 ms: 1.02x slower                                                 |
| connected_components     | 436 ms                                                                 | 445 ms: 1.02x slower                                                 |
| regex_dna                | 219 ms                                                                 | 224 ms: 1.02x slower                                                 |
| async_tree_io_tg         | 963 ms                                                                 | 987 ms: 1.02x slower                                                 |
| pathlib                  | 16.1 ms                                                                | 16.5 ms: 1.03x slower                                                |
| mdp                      | 2.72 sec                                                               | 2.79 sec: 1.03x slower                                               |
| logging_simple           | 5.48 us                                                                | 5.63 us: 1.03x slower                                                |
| logging_format           | 6.03 us                                                                | 6.20 us: 1.03x slower                                                |
| genshi_text              | 24.8 ms                                                                | 25.6 ms: 1.03x slower                                                |
| xml_etree_generate       | 79.3 ms                                                                | 82.8 ms: 1.04x slower                                                |
| xml_etree_parse          | 148 ms                                                                 | 155 ms: 1.05x slower                                                 |
| scimark_sparse_mat_mult  | 4.51 ms                                                                | 4.80 ms: 1.06x slower                                                |
| Geometric mean           | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (30): deepcopy_memo, json, async_tree_none, django_template, async_tree_cpu_io_mixed, xml_etree_process, genshi_xml, sqlglot_parse, scimark_lu, raytrace, async_tree_cpu_io_mixed_tg, async_generators, pickle_pure_python, async_tree_none_tg, deepcopy_reduce, bpe_tokeniser, coroutines, generators, scimark_sor, dulwich_log, async_tree_memoization_tg, pyflate, scimark_monte_carlo, coverage, sympy_expand, chaos, crypto_pyaes, json_dumps, async_tree_io, async_tree_memoization

- Geometric mean (including insignificant results): 1.012x faster
# HPT report

- Reliability score: 98.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x