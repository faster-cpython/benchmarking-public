
# Results vs. 3.10.4

- fork: iritkatriel
- ref: stdlib_single_arg_ex
- machine: linux-x86_64
- commit hash: 23ae36b
- commit date: 2023-01-29
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 251 ms: 1.32x faster                                                        |
| chameleon      | 8.86 ms                                                | 6.36 ms: 1.39x faster                                                       |
| docutils       | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                      |
| html5lib       | 85.8 ms                                                | 59.6 ms: 1.44x faster                                                       |
| tornado_http   | 128 ms                                                 | 93.8 ms: 1.37x faster                                                       |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 73.8 ms: 1.46x faster                                                       |
| nbody          | 136 ms                                                 | 95.6 ms: 1.43x faster                                                       |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.36x faster                                                        |
| regex_dna      | 214 ms                                                 | 202 ms: 1.06x faster                                                        |
| regex_effbot   | 3.21 ms                                                | 3.38 ms: 1.05x slower                                                       |
| regex_v8       | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.36 ms: 1.44x faster                                                       |
| json_loads           | 28.9 us                                                | 24.0 us: 1.20x faster                                                       |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                       |
| pickle_dict          | 28.3 us                                                | 31.0 us: 1.09x slower                                                       |
| pickle_list          | 4.50 us                                                | 4.22 us: 1.07x faster                                                       |
| pickle_pure_python   | 453 us                                                 | 283 us: 1.60x faster                                                        |
| unpickle             | 14.3 us                                                | 13.0 us: 1.10x faster                                                       |
| unpickle_list        | 4.99 us                                                | 4.94 us: 1.01x faster                                                       |
| unpickle_pure_python | 297 us                                                 | 199 us: 1.49x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                                        |
| xml_etree_generate   | 93.3 ms                                                | 77.1 ms: 1.21x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.93 ms: 1.56x faster                                                       |
| python_startup_no_site | 5.76 ms                                                | 6.46 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 32.3 ms: 1.43x faster                                                       |
| genshi_text     | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                       |
| genshi_xml      | 63.6 ms                                                | 47.5 ms: 1.34x faster                                                       |
| mako            | 14.3 ms                                                | 9.85 ms: 1.45x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 251 ms: 1.32x faster                                                        |
| aiohttp                 | 1.34 ms                                                | 992 us: 1.35x faster                                                        |
| async_generators        | 428 ms                                                 | 350 ms: 1.22x faster                                                        |
| async_tree_none         | 713 ms                                                 | 522 ms: 1.37x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                                      |
| async_tree_memoization  | 854 ms                                                 | 630 ms: 1.35x faster                                                        |
| chameleon               | 8.86 ms                                                | 6.36 ms: 1.39x faster                                                       |
| chaos                   | 104 ms                                                 | 64.5 ms: 1.61x faster                                                       |
| bench_thread_pool       | 943 us                                                 | 761 us: 1.24x faster                                                        |
| coroutines              | 31.7 ms                                                | 24.9 ms: 1.27x faster                                                       |
| coverage                | 75.3 ms                                                | 98.3 ms: 1.31x slower                                                       |
| crypto_pyaes            | 118 ms                                                 | 74.0 ms: 1.59x faster                                                       |
| deepcopy                | 429 us                                                 | 327 us: 1.31x faster                                                        |
| deepcopy_reduce         | 3.75 us                                                | 2.95 us: 1.27x faster                                                       |
| deepcopy_memo           | 50.0 us                                                | 34.1 us: 1.47x faster                                                       |
| deltablue               | 7.39 ms                                                | 3.20 ms: 2.31x faster                                                       |
| django_template         | 46.3 ms                                                | 32.3 ms: 1.43x faster                                                       |
| docutils                | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                      |
| dulwich_log             | 75.5 ms                                                | 62.1 ms: 1.21x faster                                                       |
| fannkuch                | 477 ms                                                 | 358 ms: 1.33x faster                                                        |
| float                   | 108 ms                                                 | 73.8 ms: 1.46x faster                                                       |
| generators              | 75.8 ms                                                | 76.9 ms: 1.02x slower                                                       |
| genshi_text             | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                       |
| genshi_xml              | 63.6 ms                                                | 47.5 ms: 1.34x faster                                                       |
| go                      | 226 ms                                                 | 133 ms: 1.70x faster                                                        |
| gunicorn                | 1.43 ms                                                | 1.06 ms: 1.35x faster                                                       |
| hexiom                  | 9.42 ms                                                | 5.86 ms: 1.61x faster                                                       |
| html5lib                | 85.8 ms                                                | 59.6 ms: 1.44x faster                                                       |
| json                    | 5.35 ms                                                | 4.58 ms: 1.17x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.36 ms: 1.44x faster                                                       |
| json_loads              | 28.9 us                                                | 24.0 us: 1.20x faster                                                       |
| logging_format          | 8.92 us                                                | 6.31 us: 1.41x faster                                                       |
| logging_silent          | 173 ns                                                 | 90.0 ns: 1.92x faster                                                       |
| logging_simple          | 8.06 us                                                | 5.72 us: 1.41x faster                                                       |
| mako                    | 14.3 ms                                                | 9.85 ms: 1.45x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.57 sec: 1.10x faster                                                      |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                        |
| mypy                    | 1.01 sec                                               | 803 ms: 1.26x faster                                                        |
| nbody                   | 136 ms                                                 | 95.6 ms: 1.43x faster                                                       |
| nqueens                 | 99.3 ms                                                | 79.1 ms: 1.26x faster                                                       |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                       |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                       |
| pickle_dict             | 28.3 us                                                | 31.0 us: 1.09x slower                                                       |
| pickle_list             | 4.50 us                                                | 4.22 us: 1.07x faster                                                       |
| pickle_pure_python      | 453 us                                                 | 283 us: 1.60x faster                                                        |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                        |
| pprint_safe_repr        | 943 ms                                                 | 670 ms: 1.41x faster                                                        |
| pprint_pformat          | 1.97 sec                                               | 1.36 sec: 1.45x faster                                                      |
| pycparser               | 1.51 sec                                               | 1.08 sec: 1.40x faster                                                      |
| pyflate                 | 675 ms                                                 | 406 ms: 1.66x faster                                                        |
| python_startup          | 13.9 ms                                                | 8.93 ms: 1.56x faster                                                       |
| python_startup_no_site  | 5.76 ms                                                | 6.46 ms: 1.12x slower                                                       |
| raytrace                | 461 ms                                                 | 280 ms: 1.65x faster                                                        |
| regex_compile           | 174 ms                                                 | 128 ms: 1.36x faster                                                        |
| regex_dna               | 214 ms                                                 | 202 ms: 1.06x faster                                                        |
| regex_effbot            | 3.21 ms                                                | 3.38 ms: 1.05x slower                                                       |
| regex_v8                | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                       |
| richards                | 71.4 ms                                                | 41.9 ms: 1.70x faster                                                       |
| scimark_fft             | 414 ms                                                 | 305 ms: 1.36x faster                                                        |
| scimark_lu              | 158 ms                                                 | 107 ms: 1.49x faster                                                        |
| scimark_monte_carlo     | 105 ms                                                 | 66.1 ms: 1.58x faster                                                       |
| scimark_sor             | 193 ms                                                 | 106 ms: 1.82x faster                                                        |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.06 ms: 1.35x faster                                                       |
| spectral_norm           | 148 ms                                                 | 94.4 ms: 1.57x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.45x faster                                                       |
| sqlglot_transpile       | 2.42 ms                                                | 1.69 ms: 1.43x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 50.7 ms: 1.29x faster                                                       |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                                        |
| sqlite_synth            | 2.90 us                                                | 2.62 us: 1.11x faster                                                       |
| sympy_expand            | 537 ms                                                 | 451 ms: 1.19x faster                                                        |
| sympy_integrate         | 23.9 ms                                                | 19.7 ms: 1.21x faster                                                       |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                        |
| sympy_str               | 324 ms                                                 | 269 ms: 1.20x faster                                                        |
| telco                   | 6.68 ms                                                | 6.38 ms: 1.05x faster                                                       |
| thrift                  | 1.03 ms                                                | 745 us: 1.38x faster                                                        |
| tornado_http            | 128 ms                                                 | 93.8 ms: 1.37x faster                                                       |
| unpack_sequence         | 59.5 ns                                                | 42.5 ns: 1.40x faster                                                       |
| unpickle                | 14.3 us                                                | 13.0 us: 1.10x faster                                                       |
| unpickle_list           | 4.99 us                                                | 4.94 us: 1.01x faster                                                       |
| unpickle_pure_python    | 297 us                                                 | 199 us: 1.49x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                        |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                                        |
| xml_etree_generate      | 93.3 ms                                                | 77.1 ms: 1.21x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                       |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230129-3.12.0a4+-23ae36b/bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
