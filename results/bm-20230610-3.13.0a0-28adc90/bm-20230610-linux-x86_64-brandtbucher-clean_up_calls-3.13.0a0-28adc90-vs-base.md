
# Results vs. base

- fork: brandtbucher
- ref: clean_up_calls
- machine: linux-x86_64
- commit hash: 28adc90
- commit date: 2023-06-10
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230609-linux-x86_64-python-33c92c4f15539806c8af-3.13.0a0-33c92c4 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.66 sec                                                              | 2.70 sec: 1.01x slower                                                |
| tornado_http   | 96.6 ms                                                               | 98.6 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230609-linux-x86_64-python-33c92c4f15539806c8af-3.13.0a0-33c92c4 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 92.8 ms                                                               | 89.1 ms: 1.04x faster                                                 |
| pidigits       | 196 ms                                                                | 196 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230609-linux-x86_64-python-33c92c4f15539806c8af-3.13.0a0-33c92c4 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 22.8 ms                                                               | 23.0 ms: 1.01x slower                                                 |
| regex_dna      | 213 ms                                                                | 216 ms: 1.01x slower                                                  |
| regex_compile  | 138 ms                                                                | 141 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230609-linux-x86_64-python-33c92c4f15539806c8af-3.13.0a0-33c92c4 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_dict          | 31.3 us                                                               | 30.2 us: 1.03x faster                                                 |
| xml_etree_generate   | 85.7 ms                                                               | 84.3 ms: 1.02x faster                                                 |
| unpickle_list        | 5.05 us                                                               | 4.96 us: 1.02x faster                                                 |
| xml_etree_parse      | 155 ms                                                                | 153 ms: 1.01x faster                                                  |
| json_dumps           | 9.86 ms                                                               | 9.72 ms: 1.01x faster                                                 |
| tomli_loads          | 2.20 sec                                                              | 2.18 sec: 1.01x faster                                                |
| xml_etree_process    | 58.8 ms                                                               | 58.2 ms: 1.01x faster                                                 |
| json_loads           | 25.5 us                                                               | 25.3 us: 1.01x faster                                                 |
| xml_etree_iterparse  | 103 ms                                                                | 104 ms: 1.01x slower                                                  |
| unpickle_pure_python | 211 us                                                                | 213 us: 1.01x slower                                                  |
| pickle               | 10.5 us                                                               | 10.6 us: 1.01x slower                                                 |
| pickle_pure_python   | 306 us                                                                | 313 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230609-linux-x86_64-python-33c92c4f15539806c8af-3.13.0a0-33c92c4 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.65 ms                                                               | 6.66 ms: 1.00x slower                                                 |
| python_startup         | 9.15 ms                                                               | 9.17 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230609-linux-x86_64-python-33c92c4f15539806c8af-3.13.0a0-33c92c4 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|-----------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.5 ms                                                               | 10.7 ms: 1.02x slower                                                 |

All benchmarks:
===============

| Benchmark              | bm-20230609-linux-x86_64-python-33c92c4f15539806c8af-3.13.0a0-33c92c4 | bm-20230610-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-28adc90 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo          | 40.8 us                                                               | 37.7 us: 1.08x faster                                                 |
| generators             | 30.7 ms                                                               | 28.6 ms: 1.07x faster                                                 |
| unpack_sequence        | 51.3 ns                                                               | 48.5 ns: 1.06x faster                                                 |
| deepcopy               | 372 us                                                                | 354 us: 1.05x faster                                                  |
| nbody                  | 92.8 ms                                                               | 89.1 ms: 1.04x faster                                                 |
| deepcopy_reduce        | 3.31 us                                                               | 3.18 us: 1.04x faster                                                 |
| spectral_norm          | 103 ms                                                                | 99.2 ms: 1.04x faster                                                 |
| json                   | 4.99 ms                                                               | 4.81 ms: 1.04x faster                                                 |
| pickle_dict            | 31.3 us                                                               | 30.2 us: 1.03x faster                                                 |
| scimark_fft            | 353 ms                                                                | 343 ms: 1.03x faster                                                  |
| scimark_monte_carlo    | 73.0 ms                                                               | 70.9 ms: 1.03x faster                                                 |
| pprint_safe_repr       | 737 ms                                                                | 722 ms: 1.02x faster                                                  |
| pprint_pformat         | 1.50 sec                                                              | 1.47 sec: 1.02x faster                                                |
| xml_etree_generate     | 85.7 ms                                                               | 84.3 ms: 1.02x faster                                                 |
| unpickle_list          | 5.05 us                                                               | 4.96 us: 1.02x faster                                                 |
| coroutines             | 22.4 ms                                                               | 22.0 ms: 1.02x faster                                                 |
| xml_etree_parse        | 155 ms                                                                | 153 ms: 1.01x faster                                                  |
| json_dumps             | 9.86 ms                                                               | 9.72 ms: 1.01x faster                                                 |
| tomli_loads            | 2.20 sec                                                              | 2.18 sec: 1.01x faster                                                |
| nqueens                | 79.5 ms                                                               | 78.7 ms: 1.01x faster                                                 |
| xml_etree_process      | 58.8 ms                                                               | 58.2 ms: 1.01x faster                                                 |
| json_loads             | 25.5 us                                                               | 25.3 us: 1.01x faster                                                 |
| scimark_sor            | 118 ms                                                                | 118 ms: 1.01x faster                                                  |
| async_generators       | 447 ms                                                                | 443 ms: 1.01x faster                                                  |
| crypto_pyaes           | 77.7 ms                                                               | 77.2 ms: 1.01x faster                                                 |
| async_tree_io          | 1.22 sec                                                              | 1.21 sec: 1.01x faster                                                |
| fannkuch               | 387 ms                                                                | 384 ms: 1.01x faster                                                  |
| create_gc_cycles       | 1.50 ms                                                               | 1.49 ms: 1.01x faster                                                 |
| mdp                    | 2.52 sec                                                              | 2.52 sec: 1.00x faster                                                |
| pidigits               | 196 ms                                                                | 196 ms: 1.00x faster                                                  |
| python_startup_no_site | 6.65 ms                                                               | 6.66 ms: 1.00x slower                                                 |
| python_startup         | 9.15 ms                                                               | 9.17 ms: 1.00x slower                                                 |
| bench_thread_pool      | 823 us                                                                | 826 us: 1.00x slower                                                  |
| asyncio_tcp_ssl        | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                |
| sqlglot_parse          | 1.31 ms                                                               | 1.32 ms: 1.00x slower                                                 |
| raytrace               | 292 ms                                                                | 294 ms: 1.00x slower                                                  |
| deltablue              | 3.22 ms                                                               | 3.24 ms: 1.01x slower                                                 |
| meteor_contest         | 105 ms                                                                | 105 ms: 1.01x slower                                                  |
| regex_v8               | 22.8 ms                                                               | 23.0 ms: 1.01x slower                                                 |
| chaos                  | 61.9 ms                                                               | 62.4 ms: 1.01x slower                                                 |
| xml_etree_iterparse    | 103 ms                                                                | 104 ms: 1.01x slower                                                  |
| async_tree_memoization | 598 ms                                                                | 604 ms: 1.01x slower                                                  |
| sqlglot_normalize      | 106 ms                                                                | 107 ms: 1.01x slower                                                  |
| sqlglot_optimize       | 53.0 ms                                                               | 53.5 ms: 1.01x slower                                                 |
| sqlite_synth           | 2.71 us                                                               | 2.74 us: 1.01x slower                                                 |
| unpickle_pure_python   | 211 us                                                                | 213 us: 1.01x slower                                                  |
| hexiom                 | 5.98 ms                                                               | 6.05 ms: 1.01x slower                                                 |
| pickle                 | 10.5 us                                                               | 10.6 us: 1.01x slower                                                 |
| logging_silent         | 97.0 ns                                                               | 98.3 ns: 1.01x slower                                                 |
| scimark_lu             | 110 ms                                                                | 111 ms: 1.01x slower                                                  |
| regex_dna              | 213 ms                                                                | 216 ms: 1.01x slower                                                  |
| docutils               | 2.66 sec                                                              | 2.70 sec: 1.01x slower                                                |
| coverage               | 93.5 ms                                                               | 94.9 ms: 1.01x slower                                                 |
| asyncio_tcp            | 508 ms                                                                | 516 ms: 1.02x slower                                                  |
| richards               | 43.8 ms                                                               | 44.5 ms: 1.02x slower                                                 |
| go                     | 133 ms                                                                | 136 ms: 1.02x slower                                                  |
| mypy2                  | 336 ms                                                                | 342 ms: 1.02x slower                                                  |
| tornado_http           | 96.6 ms                                                               | 98.6 ms: 1.02x slower                                                 |
| mako                   | 10.5 ms                                                               | 10.7 ms: 1.02x slower                                                 |
| regex_compile          | 138 ms                                                                | 141 ms: 1.02x slower                                                  |
| pickle_pure_python     | 306 us                                                                | 313 us: 1.02x slower                                                  |
| logging_simple         | 5.92 us                                                               | 6.06 us: 1.02x slower                                                 |
| richards_super         | 49.5 ms                                                               | 50.8 ms: 1.02x slower                                                 |
| pyflate                | 434 ms                                                                | 446 ms: 1.03x slower                                                  |
| dulwich_log            | 64.8 ms                                                               | 66.7 ms: 1.03x slower                                                 |
| logging_format         | 6.57 us                                                               | 6.80 us: 1.04x slower                                                 |
| gc_traversal           | 3.81 ms                                                               | 4.08 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (15): unpickle, float, pathlib, pycparser, bench_mp_pool, regex_effbot, typing_runtime_protocols, sqlglot_transpile, scimark_sparse_mat_mult, pickle_list, comprehensions, async_tree_none, dask, telco, async_tree_cpu_io_mixed
