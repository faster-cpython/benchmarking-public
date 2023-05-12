
# Results vs. base

- fork: brandtbucher
- ref: eval_frame
- machine: linux-x86_64
- commit hash: 26d9521
- commit date: 2023-05-11
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230511-linux-x86_64-python-0449ffe3a4ddf03367a5-3.12.0a7+-0449ffe | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                 | 269 ms: 1.01x faster                                               |
| docutils       | 2.71 sec                                                               | 2.72 sec: 1.01x slower                                             |
| tornado_http   | 102 ms                                                                 | 99.3 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230511-linux-x86_64-python-0449ffe3a4ddf03367a5-3.12.0a7+-0449ffe | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                 | 189 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230511-linux-x86_64-python-0449ffe3a4ddf03367a5-3.12.0a7+-0449ffe | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                                | 20.9 ms: 1.05x faster                                              |
| regex_compile  | 147 ms                                                                 | 145 ms: 1.01x faster                                               |
| regex_effbot   | 3.56 ms                                                                | 3.53 ms: 1.01x faster                                              |
| regex_dna      | 205 ms                                                                 | 203 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230511-linux-x86_64-python-0449ffe3a4ddf03367a5-3.12.0a7+-0449ffe | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|---------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_list       | 5.10 us                                                                | 4.91 us: 1.04x faster                                              |
| unpickle            | 15.4 us                                                                | 14.8 us: 1.04x faster                                              |
| tomli_loads         | 2.28 sec                                                               | 2.22 sec: 1.03x faster                                             |
| json_loads          | 25.3 us                                                                | 25.0 us: 1.02x faster                                              |
| pickle              | 10.6 us                                                                | 10.5 us: 1.01x faster                                              |
| xml_etree_generate  | 85.3 ms                                                                | 85.6 ms: 1.00x slower                                              |
| xml_etree_iterparse | 104 ms                                                                 | 104 ms: 1.01x slower                                               |
| json_dumps          | 9.88 ms                                                                | 10.0 ms: 1.02x slower                                              |
| xml_etree_parse     | 152 ms                                                                 | 155 ms: 1.02x slower                                               |
| pickle_dict         | 30.9 us                                                                | 32.2 us: 1.04x slower                                              |
| pickle_list         | 4.56 us                                                                | 4.80 us: 1.05x slower                                              |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (3): xml_etree_process, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230511-linux-x86_64-python-0449ffe3a4ddf03367a5-3.12.0a7+-0449ffe | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 9.16 ms                                                                | 9.18 ms: 1.00x slower                                              |
| python_startup_no_site | 6.68 ms                                                                | 6.71 ms: 1.00x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230511-linux-x86_64-python-0449ffe3a4ddf03367a5-3.12.0a7+-0449ffe | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|-----------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako      | 11.1 ms                                                                | 10.9 ms: 1.02x faster                                              |

All benchmarks:
===============

| Benchmark                | bm-20230511-linux-x86_64-python-0449ffe3a4ddf03367a5-3.12.0a7+-0449ffe | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| gc_traversal             | 4.31 ms                                                                | 3.93 ms: 1.10x faster                                              |
| regex_v8                 | 22.0 ms                                                                | 20.9 ms: 1.05x faster                                              |
| pycparser                | 1.21 sec                                                               | 1.15 sec: 1.05x faster                                             |
| unpack_sequence          | 48.9 ns                                                                | 46.7 ns: 1.05x faster                                              |
| unpickle_list            | 5.10 us                                                                | 4.91 us: 1.04x faster                                              |
| spectral_norm            | 109 ms                                                                 | 105 ms: 1.04x faster                                               |
| deepcopy_memo            | 39.3 us                                                                | 37.9 us: 1.04x faster                                              |
| unpickle                 | 15.4 us                                                                | 14.8 us: 1.04x faster                                              |
| logging_silent           | 105 ns                                                                 | 102 ns: 1.03x faster                                               |
| deltablue                | 3.63 ms                                                                | 3.52 ms: 1.03x faster                                              |
| tornado_http             | 102 ms                                                                 | 99.3 ms: 1.03x faster                                              |
| coroutines               | 23.4 ms                                                                | 22.7 ms: 1.03x faster                                              |
| deepcopy_reduce          | 3.25 us                                                                | 3.16 us: 1.03x faster                                              |
| tomli_loads              | 2.28 sec                                                               | 2.22 sec: 1.03x faster                                             |
| crypto_pyaes             | 79.5 ms                                                                | 77.5 ms: 1.03x faster                                              |
| logging_simple           | 6.39 us                                                                | 6.23 us: 1.03x faster                                              |
| hexiom                   | 6.34 ms                                                                | 6.22 ms: 1.02x faster                                              |
| mako                     | 11.1 ms                                                                | 10.9 ms: 1.02x faster                                              |
| scimark_sor              | 125 ms                                                                 | 123 ms: 1.02x faster                                               |
| logging_format           | 7.05 us                                                                | 6.94 us: 1.02x faster                                              |
| go                       | 138 ms                                                                 | 136 ms: 1.02x faster                                               |
| json_loads               | 25.3 us                                                                | 25.0 us: 1.02x faster                                              |
| regex_compile            | 147 ms                                                                 | 145 ms: 1.01x faster                                               |
| json                     | 4.82 ms                                                                | 4.76 ms: 1.01x faster                                              |
| pyflate                  | 454 ms                                                                 | 448 ms: 1.01x faster                                               |
| deepcopy                 | 359 us                                                                 | 354 us: 1.01x faster                                               |
| pprint_safe_repr         | 741 ms                                                                 | 733 ms: 1.01x faster                                               |
| regex_effbot             | 3.56 ms                                                                | 3.53 ms: 1.01x faster                                              |
| richards                 | 45.5 ms                                                                | 45.1 ms: 1.01x faster                                              |
| dulwich_log              | 68.5 ms                                                                | 67.8 ms: 1.01x faster                                              |
| 2to3                     | 272 ms                                                                 | 269 ms: 1.01x faster                                               |
| typing_runtime_protocols | 147 us                                                                 | 146 us: 1.01x faster                                               |
| regex_dna                | 205 ms                                                                 | 203 ms: 1.01x faster                                               |
| nqueens                  | 83.1 ms                                                                | 82.6 ms: 1.01x faster                                              |
| scimark_lu               | 115 ms                                                                 | 114 ms: 1.01x faster                                               |
| pickle                   | 10.6 us                                                                | 10.5 us: 1.01x faster                                              |
| mdp                      | 2.56 sec                                                               | 2.55 sec: 1.00x faster                                             |
| pprint_pformat           | 1.51 sec                                                               | 1.50 sec: 1.00x faster                                             |
| fannkuch                 | 388 ms                                                                 | 386 ms: 1.00x faster                                               |
| asyncio_tcp_ssl          | 1.80 sec                                                               | 1.79 sec: 1.00x faster                                             |
| pidigits                 | 189 ms                                                                 | 189 ms: 1.00x faster                                               |
| python_startup           | 9.16 ms                                                                | 9.18 ms: 1.00x slower                                              |
| python_startup_no_site   | 6.68 ms                                                                | 6.71 ms: 1.00x slower                                              |
| bench_thread_pool        | 826 us                                                                 | 829 us: 1.00x slower                                               |
| xml_etree_generate       | 85.3 ms                                                                | 85.6 ms: 1.00x slower                                              |
| docutils                 | 2.71 sec                                                               | 2.72 sec: 1.01x slower                                             |
| pathlib                  | 18.3 ms                                                                | 18.5 ms: 1.01x slower                                              |
| chaos                    | 64.9 ms                                                                | 65.4 ms: 1.01x slower                                              |
| xml_etree_iterparse      | 104 ms                                                                 | 104 ms: 1.01x slower                                               |
| async_generators         | 452 ms                                                                 | 456 ms: 1.01x slower                                               |
| async_tree_io            | 1.15 sec                                                               | 1.16 sec: 1.01x slower                                             |
| async_tree_none          | 467 ms                                                                 | 471 ms: 1.01x slower                                               |
| scimark_sparse_mat_mult  | 4.93 ms                                                                | 4.98 ms: 1.01x slower                                              |
| meteor_contest           | 104 ms                                                                 | 106 ms: 1.01x slower                                               |
| json_dumps               | 9.88 ms                                                                | 10.0 ms: 1.02x slower                                              |
| create_gc_cycles         | 1.47 ms                                                                | 1.50 ms: 1.02x slower                                              |
| asyncio_tcp              | 506 ms                                                                 | 516 ms: 1.02x slower                                               |
| xml_etree_parse          | 152 ms                                                                 | 155 ms: 1.02x slower                                               |
| pickle_dict              | 30.9 us                                                                | 32.2 us: 1.04x slower                                              |
| pickle_list              | 4.56 us                                                                | 4.80 us: 1.05x slower                                              |
| Geometric mean           | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (25): telco, sqlite_synth, sqlglot_parse, sqlalchemy_imperative, scimark_monte_carlo, richards_super, sqlglot_transpile, nbody, xml_etree_process, sqlglot_normalize, raytrace, bench_mp_pool, generators, scimark_fft, unpickle_pure_python, float, sqlglot_optimize, dask, sqlalchemy_declarative, coverage, mypy2, comprehensions, pickle_pure_python, async_tree_cpu_io_mixed, async_tree_memoization
