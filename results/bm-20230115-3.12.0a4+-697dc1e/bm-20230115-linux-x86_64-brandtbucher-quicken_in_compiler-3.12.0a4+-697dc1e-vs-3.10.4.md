
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 697dc1e
- commit date: 2023-01-15
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 251 ms: 1.32x faster                                                        |
| chameleon      | 8.86 ms                                                | 6.35 ms: 1.39x faster                                                       |
| docutils       | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                      |
| html5lib       | 85.8 ms                                                | 60.4 ms: 1.42x faster                                                       |
| tornado_http   | 128 ms                                                 | 93.8 ms: 1.37x faster                                                       |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 71.5 ms: 1.51x faster                                                       |
| nbody          | 136 ms                                                 | 94.8 ms: 1.44x faster                                                       |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.36x faster                                                        |
| regex_dna      | 214 ms                                                 | 211 ms: 1.01x faster                                                        |
| regex_effbot   | 3.21 ms                                                | 3.51 ms: 1.09x slower                                                       |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.34 ms: 1.44x faster                                                       |
| json_loads           | 28.9 us                                                | 23.9 us: 1.21x faster                                                       |
| pickle_dict          | 28.3 us                                                | 29.9 us: 1.06x slower                                                       |
| pickle_list          | 4.50 us                                                | 4.06 us: 1.11x faster                                                       |
| pickle_pure_python   | 453 us                                                 | 279 us: 1.62x faster                                                        |
| unpickle             | 14.3 us                                                | 13.2 us: 1.08x faster                                                       |
| unpickle_pure_python | 297 us                                                 | 196 us: 1.51x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 157 ms: 1.04x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                 | 109 ms: 1.01x faster                                                        |
| xml_etree_generate   | 93.3 ms                                                | 78.8 ms: 1.18x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                |

Benchmark hidden because not significant (2): pickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.68 ms: 1.61x faster                                                       |
| python_startup_no_site | 5.76 ms                                                | 6.22 ms: 1.08x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.22x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 32.0 ms: 1.44x faster                                                       |
| genshi_text     | 30.6 ms                                                | 20.1 ms: 1.52x faster                                                       |
| genshi_xml      | 63.6 ms                                                | 46.1 ms: 1.38x faster                                                       |
| mako            | 14.3 ms                                                | 9.63 ms: 1.48x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 251 ms: 1.32x faster                                                        |
| aiohttp                 | 1.34 ms                                                | 999 us: 1.34x faster                                                        |
| async_generators        | 428 ms                                                 | 348 ms: 1.23x faster                                                        |
| async_tree_none         | 713 ms                                                 | 524 ms: 1.36x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 751 ms: 1.26x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                      |
| async_tree_memoization  | 854 ms                                                 | 655 ms: 1.30x faster                                                        |
| chameleon               | 8.86 ms                                                | 6.35 ms: 1.39x faster                                                       |
| chaos                   | 104 ms                                                 | 65.5 ms: 1.59x faster                                                       |
| bench_thread_pool       | 943 us                                                 | 774 us: 1.22x faster                                                        |
| coroutines              | 31.7 ms                                                | 24.9 ms: 1.27x faster                                                       |
| coverage                | 75.3 ms                                                | 96.0 ms: 1.27x slower                                                       |
| crypto_pyaes            | 118 ms                                                 | 73.3 ms: 1.60x faster                                                       |
| deepcopy                | 429 us                                                 | 324 us: 1.33x faster                                                        |
| deepcopy_reduce         | 3.75 us                                                | 2.89 us: 1.30x faster                                                       |
| deepcopy_memo           | 50.0 us                                                | 34.4 us: 1.45x faster                                                       |
| deltablue               | 7.39 ms                                                | 3.19 ms: 2.32x faster                                                       |
| django_template         | 46.3 ms                                                | 32.0 ms: 1.44x faster                                                       |
| docutils                | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                      |
| dulwich_log             | 75.5 ms                                                | 62.1 ms: 1.22x faster                                                       |
| fannkuch                | 477 ms                                                 | 362 ms: 1.32x faster                                                        |
| float                   | 108 ms                                                 | 71.5 ms: 1.51x faster                                                       |
| generators              | 75.8 ms                                                | 75.9 ms: 1.00x slower                                                       |
| genshi_text             | 30.6 ms                                                | 20.1 ms: 1.52x faster                                                       |
| genshi_xml              | 63.6 ms                                                | 46.1 ms: 1.38x faster                                                       |
| go                      | 226 ms                                                 | 131 ms: 1.72x faster                                                        |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                                       |
| hexiom                  | 9.42 ms                                                | 6.03 ms: 1.56x faster                                                       |
| html5lib                | 85.8 ms                                                | 60.4 ms: 1.42x faster                                                       |
| json                    | 5.35 ms                                                | 4.59 ms: 1.17x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.34 ms: 1.44x faster                                                       |
| json_loads              | 28.9 us                                                | 23.9 us: 1.21x faster                                                       |
| logging_format          | 8.92 us                                                | 6.26 us: 1.43x faster                                                       |
| logging_silent          | 173 ns                                                 | 93.8 ns: 1.85x faster                                                       |
| logging_simple          | 8.06 us                                                | 5.65 us: 1.42x faster                                                       |
| mako                    | 14.3 ms                                                | 9.63 ms: 1.48x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.47 sec: 1.14x faster                                                      |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                        |
| mypy                    | 1.01 sec                                               | 808 ms: 1.25x faster                                                        |
| nbody                   | 136 ms                                                 | 94.8 ms: 1.44x faster                                                       |
| nqueens                 | 99.3 ms                                                | 78.5 ms: 1.26x faster                                                       |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                                       |
| pickle_dict             | 28.3 us                                                | 29.9 us: 1.06x slower                                                       |
| pickle_list             | 4.50 us                                                | 4.06 us: 1.11x faster                                                       |
| pickle_pure_python      | 453 us                                                 | 279 us: 1.62x faster                                                        |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                                        |
| pprint_safe_repr        | 943 ms                                                 | 670 ms: 1.41x faster                                                        |
| pprint_pformat          | 1.97 sec                                               | 1.39 sec: 1.42x faster                                                      |
| pycparser               | 1.51 sec                                               | 1.11 sec: 1.36x faster                                                      |
| pyflate                 | 675 ms                                                 | 404 ms: 1.67x faster                                                        |
| python_startup          | 13.9 ms                                                | 8.68 ms: 1.61x faster                                                       |
| python_startup_no_site  | 5.76 ms                                                | 6.22 ms: 1.08x slower                                                       |
| raytrace                | 461 ms                                                 | 283 ms: 1.63x faster                                                        |
| regex_compile           | 174 ms                                                 | 128 ms: 1.36x faster                                                        |
| regex_dna               | 214 ms                                                 | 211 ms: 1.01x faster                                                        |
| regex_effbot            | 3.21 ms                                                | 3.51 ms: 1.09x slower                                                       |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                       |
| richards                | 71.4 ms                                                | 42.0 ms: 1.70x faster                                                       |
| scimark_fft             | 414 ms                                                 | 308 ms: 1.34x faster                                                        |
| scimark_lu              | 158 ms                                                 | 109 ms: 1.46x faster                                                        |
| scimark_monte_carlo     | 105 ms                                                 | 66.4 ms: 1.58x faster                                                       |
| scimark_sor             | 193 ms                                                 | 106 ms: 1.83x faster                                                        |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.47 ms: 1.23x faster                                                       |
| spectral_norm           | 148 ms                                                 | 96.0 ms: 1.54x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                                       |
| sqlglot_transpile       | 2.42 ms                                                | 1.68 ms: 1.43x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 50.2 ms: 1.30x faster                                                       |
| sqlglot_normalize       | 135 ms                                                 | 103 ms: 1.30x faster                                                        |
| sqlite_synth            | 2.90 us                                                | 2.58 us: 1.13x faster                                                       |
| sympy_expand            | 537 ms                                                 | 452 ms: 1.19x faster                                                        |
| sympy_integrate         | 23.9 ms                                                | 20.2 ms: 1.19x faster                                                       |
| sympy_sum               | 183 ms                                                 | 162 ms: 1.13x faster                                                        |
| sympy_str               | 324 ms                                                 | 281 ms: 1.15x faster                                                        |
| telco                   | 6.68 ms                                                | 6.26 ms: 1.07x faster                                                       |
| thrift                  | 1.03 ms                                                | 742 us: 1.39x faster                                                        |
| tornado_http            | 128 ms                                                 | 93.8 ms: 1.37x faster                                                       |
| unpack_sequence         | 59.5 ns                                                | 44.9 ns: 1.33x faster                                                       |
| unpickle                | 14.3 us                                                | 13.2 us: 1.08x faster                                                       |
| unpickle_pure_python    | 297 us                                                 | 196 us: 1.51x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 157 ms: 1.04x faster                                                        |
| xml_etree_iterparse     | 110 ms                                                 | 109 ms: 1.01x faster                                                        |
| xml_etree_generate      | 93.3 ms                                                | 78.8 ms: 1.18x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                |

Benchmark hidden because not significant (3): bench_mp_pool, pickle, unpickle_list
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230115-3.12.0a4+-697dc1e/bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
