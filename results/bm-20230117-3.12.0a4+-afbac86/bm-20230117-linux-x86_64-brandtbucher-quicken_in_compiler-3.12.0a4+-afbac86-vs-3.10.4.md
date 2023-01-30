
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: afbac86
- commit date: 2023-01-17
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 252 ms: 1.32x faster                                                        |
| chameleon      | 8.86 ms                                                | 6.39 ms: 1.39x faster                                                       |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                      |
| html5lib       | 85.8 ms                                                | 60.3 ms: 1.42x faster                                                       |
| tornado_http   | 128 ms                                                 | 93.8 ms: 1.37x faster                                                       |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 73.0 ms: 1.48x faster                                                       |
| nbody          | 136 ms                                                 | 94.5 ms: 1.44x faster                                                       |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 129 ms: 1.35x faster                                                        |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.11x faster                                                       |
| regex_dna      | 214 ms                                                 | 207 ms: 1.03x faster                                                        |
| regex_effbot   | 3.21 ms                                                | 3.48 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 288 us: 1.57x faster                                                        |
| unpickle_pure_python | 297 us                                                 | 204 us: 1.46x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.35 ms: 1.44x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 54.4 ms: 1.37x faster                                                       |
| json_loads           | 28.9 us                                                | 24.1 us: 1.20x faster                                                       |
| xml_etree_generate   | 93.3 ms                                                | 78.0 ms: 1.20x faster                                                       |
| pickle_list          | 4.50 us                                                | 4.00 us: 1.13x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                                        |
| unpickle             | 14.3 us                                                | 13.2 us: 1.08x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                 | 106 ms: 1.04x faster                                                        |
| pickle               | 10.1 us                                                | 9.93 us: 1.02x faster                                                       |
| unpickle_list        | 4.99 us                                                | 5.06 us: 1.01x slower                                                       |
| pickle_dict          | 28.3 us                                                | 29.9 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.89 ms: 1.57x faster                                                       |
| python_startup_no_site | 5.76 ms                                                | 6.42 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.65 ms: 1.48x faster                                                       |
| genshi_text     | 30.6 ms                                                | 20.9 ms: 1.47x faster                                                       |
| django_template | 46.3 ms                                                | 32.0 ms: 1.44x faster                                                       |
| genshi_xml      | 63.6 ms                                                | 47.4 ms: 1.34x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.22 ms: 2.29x faster                                                       |
| logging_silent          | 173 ns                                                 | 91.2 ns: 1.90x faster                                                       |
| scimark_sor             | 193 ms                                                 | 107 ms: 1.81x faster                                                        |
| pyflate                 | 675 ms                                                 | 404 ms: 1.67x faster                                                        |
| richards                | 71.4 ms                                                | 43.0 ms: 1.66x faster                                                       |
| go                      | 226 ms                                                 | 138 ms: 1.64x faster                                                        |
| raytrace                | 461 ms                                                 | 284 ms: 1.62x faster                                                        |
| chaos                   | 104 ms                                                 | 64.3 ms: 1.62x faster                                                       |
| scimark_monte_carlo     | 105 ms                                                 | 65.2 ms: 1.61x faster                                                       |
| crypto_pyaes            | 118 ms                                                 | 73.2 ms: 1.60x faster                                                       |
| spectral_norm           | 148 ms                                                 | 93.8 ms: 1.58x faster                                                       |
| hexiom                  | 9.42 ms                                                | 5.98 ms: 1.58x faster                                                       |
| pickle_pure_python      | 453 us                                                 | 288 us: 1.57x faster                                                        |
| python_startup          | 13.9 ms                                                | 8.89 ms: 1.57x faster                                                       |
| scimark_lu              | 158 ms                                                 | 107 ms: 1.48x faster                                                        |
| mako                    | 14.3 ms                                                | 9.65 ms: 1.48x faster                                                       |
| float                   | 108 ms                                                 | 73.0 ms: 1.48x faster                                                       |
| genshi_text             | 30.6 ms                                                | 20.9 ms: 1.47x faster                                                       |
| unpickle_pure_python    | 297 us                                                 | 204 us: 1.46x faster                                                        |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.45x faster                                                       |
| deepcopy_memo           | 50.0 us                                                | 34.5 us: 1.45x faster                                                       |
| django_template         | 46.3 ms                                                | 32.0 ms: 1.44x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.35 ms: 1.44x faster                                                       |
| nbody                   | 136 ms                                                 | 94.5 ms: 1.44x faster                                                       |
| unpack_sequence         | 59.5 ns                                                | 41.4 ns: 1.43x faster                                                       |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                                      |
| sqlglot_transpile       | 2.42 ms                                                | 1.70 ms: 1.42x faster                                                       |
| html5lib                | 85.8 ms                                                | 60.3 ms: 1.42x faster                                                       |
| pprint_safe_repr        | 943 ms                                                 | 671 ms: 1.40x faster                                                        |
| thrift                  | 1.03 ms                                                | 739 us: 1.40x faster                                                        |
| chameleon               | 8.86 ms                                                | 6.39 ms: 1.39x faster                                                       |
| logging_format          | 8.92 us                                                | 6.45 us: 1.38x faster                                                       |
| logging_simple          | 8.06 us                                                | 5.82 us: 1.38x faster                                                       |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.00 ms: 1.37x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 54.4 ms: 1.37x faster                                                       |
| tornado_http            | 128 ms                                                 | 93.8 ms: 1.37x faster                                                       |
| async_tree_none         | 713 ms                                                 | 525 ms: 1.36x faster                                                        |
| scimark_fft             | 414 ms                                                 | 306 ms: 1.35x faster                                                        |
| regex_compile           | 174 ms                                                 | 129 ms: 1.35x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.34x faster                                                      |
| genshi_xml              | 63.6 ms                                                | 47.4 ms: 1.34x faster                                                       |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                                       |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                       |
| 2to3                    | 332 ms                                                 | 252 ms: 1.32x faster                                                        |
| pycparser               | 1.51 sec                                               | 1.15 sec: 1.31x faster                                                      |
| deepcopy                | 429 us                                                 | 328 us: 1.31x faster                                                        |
| nqueens                 | 99.3 ms                                                | 76.6 ms: 1.30x faster                                                       |
| async_tree_memoization  | 854 ms                                                 | 659 ms: 1.30x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                        |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                       |
| coroutines              | 31.7 ms                                                | 24.8 ms: 1.27x faster                                                       |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                      |
| deepcopy_reduce         | 3.75 us                                                | 2.95 us: 1.27x faster                                                       |
| fannkuch                | 477 ms                                                 | 376 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 752 ms: 1.26x faster                                                        |
| mypy                    | 1.01 sec                                               | 805 ms: 1.26x faster                                                        |
| dulwich_log             | 75.5 ms                                                | 62.2 ms: 1.21x faster                                                       |
| bench_thread_pool       | 943 us                                                 | 778 us: 1.21x faster                                                        |
| sympy_integrate         | 23.9 ms                                                | 19.8 ms: 1.21x faster                                                       |
| async_generators        | 428 ms                                                 | 354 ms: 1.21x faster                                                        |
| sympy_str               | 324 ms                                                 | 269 ms: 1.20x faster                                                        |
| json_loads              | 28.9 us                                                | 24.1 us: 1.20x faster                                                       |
| xml_etree_generate      | 93.3 ms                                                | 78.0 ms: 1.20x faster                                                       |
| sympy_expand            | 537 ms                                                 | 454 ms: 1.18x faster                                                        |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                        |
| json                    | 5.35 ms                                                | 4.66 ms: 1.15x faster                                                       |
| sqlite_synth            | 2.90 us                                                | 2.56 us: 1.13x faster                                                       |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                       |
| pickle_list             | 4.50 us                                                | 4.00 us: 1.13x faster                                                       |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.11x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.56 sec: 1.10x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                                        |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                        |
| unpickle                | 14.3 us                                                | 13.2 us: 1.08x faster                                                       |
| telco                   | 6.68 ms                                                | 6.35 ms: 1.05x faster                                                       |
| xml_etree_iterparse     | 110 ms                                                 | 106 ms: 1.04x faster                                                        |
| regex_dna               | 214 ms                                                 | 207 ms: 1.03x faster                                                        |
| pickle                  | 10.1 us                                                | 9.93 us: 1.02x faster                                                       |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                                        |
| generators              | 75.8 ms                                                | 76.6 ms: 1.01x slower                                                       |
| unpickle_list           | 4.99 us                                                | 5.06 us: 1.01x slower                                                       |
| pickle_dict             | 28.3 us                                                | 29.9 us: 1.06x slower                                                       |
| regex_effbot            | 3.21 ms                                                | 3.48 ms: 1.08x slower                                                       |
| python_startup_no_site  | 5.76 ms                                                | 6.42 ms: 1.11x slower                                                       |
| coverage                | 75.3 ms                                                | 93.1 ms: 1.24x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230117-3.12.0a4+-afbac86/bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
