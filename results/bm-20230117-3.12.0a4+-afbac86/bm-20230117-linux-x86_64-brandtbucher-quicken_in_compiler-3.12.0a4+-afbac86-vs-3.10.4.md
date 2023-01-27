
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
| 2to3           | 332 ms                                                 | 251 ms: 1.32x faster                                                        |
| chameleon      | 8.86 ms                                                | 6.43 ms: 1.38x faster                                                       |
| docutils       | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                      |
| html5lib       | 85.8 ms                                                | 59.9 ms: 1.43x faster                                                       |
| tornado_http   | 128 ms                                                 | 94.3 ms: 1.36x faster                                                       |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.0 ms: 1.50x faster                                                       |
| nbody          | 136 ms                                                 | 94.1 ms: 1.45x faster                                                       |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.36x faster                                                        |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                        |
| regex_effbot   | 3.21 ms                                                | 3.52 ms: 1.10x slower                                                       |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.36 ms: 1.44x faster                                                       |
| json_loads           | 28.9 us                                                | 23.8 us: 1.21x faster                                                       |
| pickle_dict          | 28.3 us                                                | 30.9 us: 1.09x slower                                                       |
| pickle_list          | 4.50 us                                                | 4.10 us: 1.10x faster                                                       |
| pickle_pure_python   | 453 us                                                 | 288 us: 1.58x faster                                                        |
| unpickle             | 14.3 us                                                | 13.2 us: 1.08x faster                                                       |
| unpickle_list        | 4.99 us                                                | 5.24 us: 1.05x slower                                                       |
| unpickle_pure_python | 297 us                                                 | 201 us: 1.48x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                                        |
| xml_etree_generate   | 93.3 ms                                                | 77.2 ms: 1.21x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 53.9 ms: 1.38x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.84 ms: 1.58x faster                                                       |
| python_startup_no_site | 5.76 ms                                                | 6.39 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 32.4 ms: 1.43x faster                                                       |
| genshi_text     | 30.6 ms                                                | 21.1 ms: 1.45x faster                                                       |
| genshi_xml      | 63.6 ms                                                | 47.3 ms: 1.34x faster                                                       |
| mako            | 14.3 ms                                                | 9.75 ms: 1.46x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 251 ms: 1.32x faster                                                        |
| aiohttp                 | 1.34 ms                                                | 993 us: 1.35x faster                                                        |
| async_generators        | 428 ms                                                 | 351 ms: 1.22x faster                                                        |
| async_tree_none         | 713 ms                                                 | 520 ms: 1.37x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.36x faster                                                      |
| async_tree_memoization  | 854 ms                                                 | 646 ms: 1.32x faster                                                        |
| chameleon               | 8.86 ms                                                | 6.43 ms: 1.38x faster                                                       |
| chaos                   | 104 ms                                                 | 64.2 ms: 1.62x faster                                                       |
| bench_thread_pool       | 943 us                                                 | 778 us: 1.21x faster                                                        |
| coroutines              | 31.7 ms                                                | 24.5 ms: 1.29x faster                                                       |
| coverage                | 75.3 ms                                                | 93.5 ms: 1.24x slower                                                       |
| crypto_pyaes            | 118 ms                                                 | 72.2 ms: 1.63x faster                                                       |
| deepcopy                | 429 us                                                 | 328 us: 1.31x faster                                                        |
| deepcopy_reduce         | 3.75 us                                                | 2.93 us: 1.28x faster                                                       |
| deepcopy_memo           | 50.0 us                                                | 34.4 us: 1.45x faster                                                       |
| deltablue               | 7.39 ms                                                | 3.23 ms: 2.29x faster                                                       |
| django_template         | 46.3 ms                                                | 32.4 ms: 1.43x faster                                                       |
| docutils                | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                      |
| dulwich_log             | 75.5 ms                                                | 62.4 ms: 1.21x faster                                                       |
| fannkuch                | 477 ms                                                 | 366 ms: 1.30x faster                                                        |
| float                   | 108 ms                                                 | 72.0 ms: 1.50x faster                                                       |
| generators              | 75.8 ms                                                | 77.0 ms: 1.02x slower                                                       |
| genshi_text             | 30.6 ms                                                | 21.1 ms: 1.45x faster                                                       |
| genshi_xml              | 63.6 ms                                                | 47.3 ms: 1.34x faster                                                       |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                        |
| gunicorn                | 1.43 ms                                                | 1.06 ms: 1.35x faster                                                       |
| hexiom                  | 9.42 ms                                                | 6.13 ms: 1.54x faster                                                       |
| html5lib                | 85.8 ms                                                | 59.9 ms: 1.43x faster                                                       |
| json                    | 5.35 ms                                                | 4.55 ms: 1.18x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.36 ms: 1.44x faster                                                       |
| json_loads              | 28.9 us                                                | 23.8 us: 1.21x faster                                                       |
| logging_format          | 8.92 us                                                | 6.42 us: 1.39x faster                                                       |
| logging_silent          | 173 ns                                                 | 90.1 ns: 1.92x faster                                                       |
| logging_simple          | 8.06 us                                                | 5.83 us: 1.38x faster                                                       |
| mako                    | 14.3 ms                                                | 9.75 ms: 1.46x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.61 sec: 1.08x faster                                                      |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.08x faster                                                        |
| mypy                    | 1.01 sec                                               | 802 ms: 1.26x faster                                                        |
| nbody                   | 136 ms                                                 | 94.1 ms: 1.45x faster                                                       |
| nqueens                 | 99.3 ms                                                | 76.3 ms: 1.30x faster                                                       |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                       |
| pickle_dict             | 28.3 us                                                | 30.9 us: 1.09x slower                                                       |
| pickle_list             | 4.50 us                                                | 4.10 us: 1.10x faster                                                       |
| pickle_pure_python      | 453 us                                                 | 288 us: 1.58x faster                                                        |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                        |
| pprint_safe_repr        | 943 ms                                                 | 677 ms: 1.39x faster                                                        |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                                      |
| pycparser               | 1.51 sec                                               | 1.14 sec: 1.33x faster                                                      |
| pyflate                 | 675 ms                                                 | 414 ms: 1.63x faster                                                        |
| python_startup          | 13.9 ms                                                | 8.84 ms: 1.58x faster                                                       |
| python_startup_no_site  | 5.76 ms                                                | 6.39 ms: 1.11x slower                                                       |
| raytrace                | 461 ms                                                 | 284 ms: 1.62x faster                                                        |
| regex_compile           | 174 ms                                                 | 128 ms: 1.36x faster                                                        |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                        |
| regex_effbot            | 3.21 ms                                                | 3.52 ms: 1.10x slower                                                       |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                       |
| richards                | 71.4 ms                                                | 42.4 ms: 1.68x faster                                                       |
| scimark_fft             | 414 ms                                                 | 302 ms: 1.37x faster                                                        |
| scimark_lu              | 158 ms                                                 | 108 ms: 1.47x faster                                                        |
| scimark_monte_carlo     | 105 ms                                                 | 66.1 ms: 1.59x faster                                                       |
| scimark_sor             | 193 ms                                                 | 106 ms: 1.82x faster                                                        |
| scimark_sparse_mat_mult | 5.48 ms                                                | 3.98 ms: 1.38x faster                                                       |
| spectral_norm           | 148 ms                                                 | 94.5 ms: 1.57x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                                       |
| sqlglot_transpile       | 2.42 ms                                                | 1.70 ms: 1.42x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                       |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                        |
| sqlite_synth            | 2.90 us                                                | 2.59 us: 1.12x faster                                                       |
| sympy_expand            | 537 ms                                                 | 454 ms: 1.18x faster                                                        |
| sympy_integrate         | 23.9 ms                                                | 19.7 ms: 1.21x faster                                                       |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.19x faster                                                        |
| sympy_str               | 324 ms                                                 | 270 ms: 1.20x faster                                                        |
| telco                   | 6.68 ms                                                | 6.45 ms: 1.04x faster                                                       |
| thrift                  | 1.03 ms                                                | 737 us: 1.40x faster                                                        |
| tornado_http            | 128 ms                                                 | 94.3 ms: 1.36x faster                                                       |
| unpack_sequence         | 59.5 ns                                                | 43.2 ns: 1.38x faster                                                       |
| unpickle                | 14.3 us                                                | 13.2 us: 1.08x faster                                                       |
| unpickle_list           | 4.99 us                                                | 5.24 us: 1.05x slower                                                       |
| unpickle_pure_python    | 297 us                                                 | 201 us: 1.48x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                        |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                                        |
| xml_etree_generate      | 93.3 ms                                                | 77.2 ms: 1.21x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 53.9 ms: 1.38x faster                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230117-3.12.0a4+-afbac86/bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
