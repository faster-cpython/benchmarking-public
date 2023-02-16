
# Results vs. 3.10.4

- fork: brandtbucher
- ref: compressed_bytecode
- machine: linux-x86_64
- commit hash: bcd7980
- commit date: 2022-12-17
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 253 ms: 1.33x faster                                                        |
| chameleon      | 9.17 ms                                                | 6.43 ms: 1.43x faster                                                       |
| docutils       | 3.18 sec                                               | 2.49 sec: 1.27x faster                                                      |
| html5lib       | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                       |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.6 ms: 1.54x faster                                                       |
| float          | 109 ms                                                 | 72.3 ms: 1.51x faster                                                       |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                                        |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                       |
| regex_dna      | 214 ms                                                 | 219 ms: 1.02x slower                                                        |
| regex_effbot   | 3.19 ms                                                | 3.58 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 282 us: 1.60x faster                                                        |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.52x faster                                                        |
| json_dumps           | 13.4 ms                                                | 9.49 ms: 1.42x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 53.6 ms: 1.39x faster                                                       |
| xml_etree_generate   | 93.8 ms                                                | 77.2 ms: 1.22x faster                                                       |
| json_loads           | 28.7 us                                                | 24.0 us: 1.20x faster                                                       |
| pickle_list          | 4.72 us                                                | 4.12 us: 1.15x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.08x faster                                                        |
| unpickle             | 14.2 us                                                | 13.3 us: 1.07x faster                                                       |
| pickle               | 10.2 us                                                | 10.2 us: 1.01x slower                                                       |
| unpickle_list        | 4.92 us                                                | 5.12 us: 1.04x slower                                                       |
| pickle_dict          | 27.6 us                                                | 30.6 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.50 ms: 1.66x faster                                                       |
| python_startup_no_site | 5.78 ms                                                | 6.08 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.72 ms: 1.51x faster                                                       |
| genshi_text     | 30.6 ms                                                | 21.3 ms: 1.44x faster                                                       |
| django_template | 46.3 ms                                                | 32.9 ms: 1.41x faster                                                       |
| genshi_xml      | 63.7 ms                                                | 47.0 ms: 1.36x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.22 ms: 2.26x faster                                                       |
| logging_silent          | 176 ns                                                 | 92.1 ns: 1.91x faster                                                       |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                                        |
| richards                | 75.2 ms                                                | 41.6 ms: 1.81x faster                                                       |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                        |
| raytrace                | 467 ms                                                 | 280 ms: 1.67x faster                                                        |
| pyflate                 | 676 ms                                                 | 407 ms: 1.66x faster                                                        |
| python_startup          | 14.1 ms                                                | 8.50 ms: 1.66x faster                                                       |
| scimark_monte_carlo     | 109 ms                                                 | 66.1 ms: 1.64x faster                                                       |
| pickle_pure_python      | 452 us                                                 | 282 us: 1.60x faster                                                        |
| chaos                   | 106 ms                                                 | 66.1 ms: 1.60x faster                                                       |
| crypto_pyaes            | 117 ms                                                 | 74.1 ms: 1.57x faster                                                       |
| spectral_norm           | 150 ms                                                 | 96.1 ms: 1.56x faster                                                       |
| hexiom                  | 9.43 ms                                                | 6.08 ms: 1.55x faster                                                       |
| deepcopy_memo           | 51.7 us                                                | 33.5 us: 1.54x faster                                                       |
| nbody                   | 144 ms                                                 | 93.6 ms: 1.54x faster                                                       |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.52x faster                                                        |
| scimark_lu              | 161 ms                                                 | 106 ms: 1.51x faster                                                        |
| float                   | 109 ms                                                 | 72.3 ms: 1.51x faster                                                       |
| mako                    | 14.7 ms                                                | 9.72 ms: 1.51x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.39 ms: 1.46x faster                                                       |
| sqlglot_transpile       | 2.43 ms                                                | 1.69 ms: 1.44x faster                                                       |
| genshi_text             | 30.6 ms                                                | 21.3 ms: 1.44x faster                                                       |
| html5lib                | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                       |
| unpack_sequence         | 59.4 ns                                                | 41.6 ns: 1.43x faster                                                       |
| chameleon               | 9.17 ms                                                | 6.43 ms: 1.43x faster                                                       |
| logging_simple          | 8.10 us                                                | 5.69 us: 1.42x faster                                                       |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.42x faster                                                      |
| json_dumps              | 13.4 ms                                                | 9.49 ms: 1.42x faster                                                       |
| logging_format          | 8.85 us                                                | 6.28 us: 1.41x faster                                                       |
| pprint_safe_repr        | 953 ms                                                 | 677 ms: 1.41x faster                                                        |
| django_template         | 46.3 ms                                                | 32.9 ms: 1.41x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 53.6 ms: 1.39x faster                                                       |
| thrift                  | 1.03 ms                                                | 745 us: 1.39x faster                                                        |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                                        |
| pycparser               | 1.53 sec                                               | 1.13 sec: 1.36x faster                                                      |
| genshi_xml              | 63.7 ms                                                | 47.0 ms: 1.36x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.03 ms: 1.35x faster                                                       |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                      |
| async_tree_memoization  | 855 ms                                                 | 635 ms: 1.35x faster                                                        |
| deepcopy                | 438 us                                                 | 326 us: 1.34x faster                                                        |
| scimark_fft             | 421 ms                                                 | 315 ms: 1.34x faster                                                        |
| async_tree_none         | 711 ms                                                 | 533 ms: 1.33x faster                                                        |
| 2to3                    | 335 ms                                                 | 253 ms: 1.33x faster                                                        |
| deepcopy_reduce         | 3.79 us                                                | 2.88 us: 1.31x faster                                                       |
| fannkuch                | 488 ms                                                 | 372 ms: 1.31x faster                                                        |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.30x faster                                                        |
| sqlglot_optimize        | 65.2 ms                                                | 50.5 ms: 1.29x faster                                                       |
| nqueens                 | 100 ms                                                 | 78.5 ms: 1.27x faster                                                       |
| docutils                | 3.18 sec                                               | 2.49 sec: 1.27x faster                                                      |
| coroutines              | 31.6 ms                                                | 25.0 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed | 949 ms                                                 | 765 ms: 1.24x faster                                                        |
| dulwich_log             | 75.8 ms                                                | 62.0 ms: 1.22x faster                                                       |
| bench_thread_pool       | 946 us                                                 | 774 us: 1.22x faster                                                        |
| xml_etree_generate      | 93.8 ms                                                | 77.2 ms: 1.22x faster                                                       |
| async_generators        | 426 ms                                                 | 355 ms: 1.20x faster                                                        |
| json_loads              | 28.7 us                                                | 24.0 us: 1.20x faster                                                       |
| sympy_integrate         | 24.0 ms                                                | 20.2 ms: 1.19x faster                                                       |
| sympy_expand            | 534 ms                                                 | 449 ms: 1.19x faster                                                        |
| sympy_str               | 325 ms                                                 | 282 ms: 1.15x faster                                                        |
| pickle_list             | 4.72 us                                                | 4.12 us: 1.15x faster                                                       |
| sqlite_synth            | 2.92 us                                                | 2.56 us: 1.14x faster                                                       |
| sympy_sum               | 183 ms                                                 | 161 ms: 1.14x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.13x faster                                                       |
| djangocms               | 36.9 us                                                | 32.6 us: 1.13x faster                                                       |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                       |
| json                    | 5.35 ms                                                | 4.80 ms: 1.11x faster                                                       |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                        |
| telco                   | 6.73 ms                                                | 6.17 ms: 1.09x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.08x faster                                                        |
| mdp                     | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                      |
| unpickle                | 14.2 us                                                | 13.3 us: 1.07x faster                                                       |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| pickle                  | 10.2 us                                                | 10.2 us: 1.01x slower                                                       |
| generators              | 76.4 ms                                                | 77.6 ms: 1.02x slower                                                       |
| regex_dna               | 214 ms                                                 | 219 ms: 1.02x slower                                                        |
| unpickle_list           | 4.92 us                                                | 5.12 us: 1.04x slower                                                       |
| python_startup_no_site  | 5.78 ms                                                | 6.08 ms: 1.05x slower                                                       |
| pickle_dict             | 27.6 us                                                | 30.6 us: 1.11x slower                                                       |
| regex_effbot            | 3.19 ms                                                | 3.58 ms: 1.12x slower                                                       |
| coverage                | 74.7 ms                                                | 99.4 ms: 1.33x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221217-3.12.0a3+-bcd7980/bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980.json: mypy
