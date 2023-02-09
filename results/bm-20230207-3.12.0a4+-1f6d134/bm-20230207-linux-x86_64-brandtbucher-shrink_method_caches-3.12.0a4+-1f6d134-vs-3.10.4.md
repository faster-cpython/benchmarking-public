
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_method_caches
- machine: linux-x86_64
- commit hash: 1f6d134
- commit date: 2023-02-07
- overall geometric mean: 1.28x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 253 ms: 1.31x faster                                                         |
| chameleon      | 8.86 ms                                                | 6.58 ms: 1.35x faster                                                        |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                       |
| html5lib       | 85.8 ms                                                | 61.3 ms: 1.40x faster                                                        |
| tornado_http   | 128 ms                                                 | 96.2 ms: 1.33x faster                                                        |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 74.0 ms: 1.46x faster                                                        |
| nbody          | 136 ms                                                 | 95.8 ms: 1.42x faster                                                        |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.35x faster                                                         |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                        |
| regex_dna      | 214 ms                                                 | 207 ms: 1.03x faster                                                         |
| regex_effbot   | 3.21 ms                                                | 3.76 ms: 1.17x slower                                                        |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 292 us: 1.55x faster                                                         |
| unpickle_pure_python | 297 us                                                 | 199 us: 1.49x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.47 ms: 1.42x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 53.8 ms: 1.38x faster                                                        |
| json_loads           | 28.9 us                                                | 23.8 us: 1.21x faster                                                        |
| xml_etree_generate   | 93.3 ms                                                | 77.6 ms: 1.20x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| pickle_list          | 4.50 us                                                | 4.05 us: 1.11x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.08x faster                                                         |
| pickle               | 10.1 us                                                | 9.96 us: 1.02x faster                                                        |
| unpickle_list        | 4.99 us                                                | 5.04 us: 1.01x slower                                                        |
| pickle_dict          | 28.3 us                                                | 30.0 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.94 ms: 1.56x faster                                                        |
| python_startup_no_site | 5.76 ms                                                | 6.45 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 21.0 ms: 1.46x faster                                                        |
| mako            | 14.3 ms                                                | 9.98 ms: 1.43x faster                                                        |
| django_template | 46.3 ms                                                | 33.2 ms: 1.39x faster                                                        |
| genshi_xml      | 63.6 ms                                                | 47.3 ms: 1.34x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.35 ms: 2.21x faster                                                        |
| scimark_sor             | 193 ms                                                 | 107 ms: 1.81x faster                                                         |
| logging_silent          | 173 ns                                                 | 99.9 ns: 1.73x faster                                                        |
| pyflate                 | 675 ms                                                 | 412 ms: 1.64x faster                                                         |
| go                      | 226 ms                                                 | 140 ms: 1.62x faster                                                         |
| raytrace                | 461 ms                                                 | 288 ms: 1.60x faster                                                         |
| richards                | 71.4 ms                                                | 44.6 ms: 1.60x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 73.7 ms: 1.59x faster                                                        |
| scimark_monte_carlo     | 105 ms                                                 | 65.8 ms: 1.59x faster                                                        |
| chaos                   | 104 ms                                                 | 65.9 ms: 1.58x faster                                                        |
| spectral_norm           | 148 ms                                                 | 94.6 ms: 1.56x faster                                                        |
| hexiom                  | 9.42 ms                                                | 6.02 ms: 1.56x faster                                                        |
| python_startup          | 13.9 ms                                                | 8.94 ms: 1.56x faster                                                        |
| pickle_pure_python      | 453 us                                                 | 292 us: 1.55x faster                                                         |
| unpickle_pure_python    | 297 us                                                 | 199 us: 1.49x faster                                                         |
| genshi_text             | 30.6 ms                                                | 21.0 ms: 1.46x faster                                                        |
| float                   | 108 ms                                                 | 74.0 ms: 1.46x faster                                                        |
| scimark_lu              | 158 ms                                                 | 111 ms: 1.43x faster                                                         |
| mako                    | 14.3 ms                                                | 9.98 ms: 1.43x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.47 ms: 1.42x faster                                                        |
| nbody                   | 136 ms                                                 | 95.8 ms: 1.42x faster                                                        |
| pprint_pformat          | 1.97 sec                                               | 1.40 sec: 1.41x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.45 ms: 1.41x faster                                                        |
| deepcopy_memo           | 50.0 us                                                | 35.7 us: 1.40x faster                                                        |
| html5lib                | 85.8 ms                                                | 61.3 ms: 1.40x faster                                                        |
| logging_simple          | 8.06 us                                                | 5.78 us: 1.39x faster                                                        |
| django_template         | 46.3 ms                                                | 33.2 ms: 1.39x faster                                                        |
| sqlglot_transpile       | 2.42 ms                                                | 1.74 ms: 1.39x faster                                                        |
| thrift                  | 1.03 ms                                                | 745 us: 1.39x faster                                                         |
| xml_etree_process       | 74.5 ms                                                | 53.8 ms: 1.38x faster                                                        |
| logging_format          | 8.92 us                                                | 6.46 us: 1.38x faster                                                        |
| pycparser               | 1.51 sec                                               | 1.09 sec: 1.38x faster                                                       |
| pprint_safe_repr        | 943 ms                                                 | 684 ms: 1.38x faster                                                         |
| async_tree_none         | 713 ms                                                 | 525 ms: 1.36x faster                                                         |
| regex_compile           | 174 ms                                                 | 128 ms: 1.35x faster                                                         |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                       |
| unpack_sequence         | 59.5 ns                                                | 44.2 ns: 1.35x faster                                                        |
| chameleon               | 8.86 ms                                                | 6.58 ms: 1.35x faster                                                        |
| genshi_xml              | 63.6 ms                                                | 47.3 ms: 1.34x faster                                                        |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.11 ms: 1.33x faster                                                        |
| tornado_http            | 128 ms                                                 | 96.2 ms: 1.33x faster                                                        |
| scimark_fft             | 414 ms                                                 | 312 ms: 1.33x faster                                                         |
| aiohttp                 | 1.34 ms                                                | 1.02 ms: 1.32x faster                                                        |
| 2to3                    | 332 ms                                                 | 253 ms: 1.31x faster                                                         |
| fannkuch                | 477 ms                                                 | 365 ms: 1.31x faster                                                         |
| gunicorn                | 1.43 ms                                                | 1.10 ms: 1.30x faster                                                        |
| nqueens                 | 99.3 ms                                                | 76.5 ms: 1.30x faster                                                        |
| async_tree_memoization  | 854 ms                                                 | 664 ms: 1.29x faster                                                         |
| async_tree_cpu_io_mixed | 949 ms                                                 | 753 ms: 1.26x faster                                                         |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 52.0 ms: 1.26x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 108 ms: 1.26x faster                                                         |
| coroutines              | 31.7 ms                                                | 25.3 ms: 1.25x faster                                                        |
| deepcopy                | 429 us                                                 | 343 us: 1.25x faster                                                         |
| deepcopy_reduce         | 3.75 us                                                | 3.01 us: 1.25x faster                                                        |
| json_loads              | 28.9 us                                                | 23.8 us: 1.21x faster                                                        |
| async_generators        | 428 ms                                                 | 354 ms: 1.21x faster                                                         |
| xml_etree_generate      | 93.3 ms                                                | 77.6 ms: 1.20x faster                                                        |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                                         |
| sympy_integrate         | 23.9 ms                                                | 20.0 ms: 1.20x faster                                                        |
| bench_thread_pool       | 943 us                                                 | 795 us: 1.19x faster                                                         |
| sympy_str               | 324 ms                                                 | 274 ms: 1.18x faster                                                         |
| sqlalchemy_imperative   | 21.0 ms                                                | 17.8 ms: 1.18x faster                                                        |
| sympy_expand            | 537 ms                                                 | 457 ms: 1.17x faster                                                         |
| dulwich_log             | 75.5 ms                                                | 64.5 ms: 1.17x faster                                                        |
| sympy_sum               | 183 ms                                                 | 157 ms: 1.16x faster                                                         |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.48 sec: 1.14x faster                                                       |
| sqlite_synth            | 2.90 us                                                | 2.58 us: 1.12x faster                                                        |
| json                    | 5.35 ms                                                | 4.79 ms: 1.12x faster                                                        |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| pickle_list             | 4.50 us                                                | 4.05 us: 1.11x faster                                                        |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                         |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.08x faster                                                         |
| telco                   | 6.68 ms                                                | 6.40 ms: 1.04x faster                                                        |
| regex_dna               | 214 ms                                                 | 207 ms: 1.03x faster                                                         |
| pickle                  | 10.1 us                                                | 9.96 us: 1.02x faster                                                        |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                         |
| unpickle_list           | 4.99 us                                                | 5.04 us: 1.01x slower                                                        |
| generators              | 75.8 ms                                                | 78.6 ms: 1.04x slower                                                        |
| pickle_dict             | 28.3 us                                                | 30.0 us: 1.06x slower                                                        |
| python_startup_no_site  | 5.76 ms                                                | 6.45 ms: 1.12x slower                                                        |
| regex_effbot            | 3.21 ms                                                | 3.76 ms: 1.17x slower                                                        |
| coverage                | 75.3 ms                                                | 99.2 ms: 1.32x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.28x faster                                                                 |

Benchmark hidden because not significant (2): unpickle, bench_mp_pool
Ignored benchmarks (3) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy, pylint
Ignored benchmarks (6) of /home/mdboom/Work/builds/benchmarking/results/bm-20230207-3.12.0a4+-1f6d134/bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal, mypy2
