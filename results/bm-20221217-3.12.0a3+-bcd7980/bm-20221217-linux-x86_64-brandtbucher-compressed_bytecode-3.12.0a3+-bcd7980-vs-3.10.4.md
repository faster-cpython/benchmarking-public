
# Results vs. 3.10.4

- fork: brandtbucher
- ref: compressed_bytecode
- machine: linux-x86_64
- commit hash: bcd7980
- commit date: 2022-12-17
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 253 ms: 1.31x faster                                                        |
| chameleon      | 8.86 ms                                                | 6.43 ms: 1.38x faster                                                       |
| docutils       | 3.18 sec                                               | 2.49 sec: 1.28x faster                                                      |
| html5lib       | 85.8 ms                                                | 59.7 ms: 1.44x faster                                                       |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.3 ms: 1.49x faster                                                       |
| nbody          | 136 ms                                                 | 93.6 ms: 1.46x faster                                                       |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 130 ms: 1.34x faster                                                        |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                       |
| regex_dna      | 214 ms                                                 | 219 ms: 1.02x slower                                                        |
| regex_effbot   | 3.21 ms                                                | 3.58 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 282 us: 1.61x faster                                                        |
| unpickle_pure_python | 297 us                                                 | 199 us: 1.49x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.49 ms: 1.42x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 53.6 ms: 1.39x faster                                                       |
| xml_etree_generate   | 93.3 ms                                                | 77.2 ms: 1.21x faster                                                       |
| json_loads           | 28.9 us                                                | 24.0 us: 1.20x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                        |
| pickle_list          | 4.50 us                                                | 4.12 us: 1.09x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                                        |
| unpickle             | 14.3 us                                                | 13.3 us: 1.07x faster                                                       |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                       |
| unpickle_list        | 4.99 us                                                | 5.12 us: 1.03x slower                                                       |
| pickle_dict          | 28.3 us                                                | 30.6 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.50 ms: 1.64x faster                                                       |
| python_startup_no_site | 5.76 ms                                                | 6.08 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.72 ms: 1.47x faster                                                       |
| genshi_text     | 30.6 ms                                                | 21.3 ms: 1.44x faster                                                       |
| django_template | 46.3 ms                                                | 32.9 ms: 1.40x faster                                                       |
| genshi_xml      | 63.6 ms                                                | 47.0 ms: 1.35x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.22 ms: 2.30x faster                                                       |
| logging_silent          | 173 ns                                                 | 92.1 ns: 1.88x faster                                                       |
| scimark_sor             | 193 ms                                                 | 105 ms: 1.84x faster                                                        |
| richards                | 71.4 ms                                                | 41.6 ms: 1.72x faster                                                       |
| go                      | 226 ms                                                 | 135 ms: 1.68x faster                                                        |
| pyflate                 | 675 ms                                                 | 407 ms: 1.66x faster                                                        |
| raytrace                | 461 ms                                                 | 280 ms: 1.65x faster                                                        |
| python_startup          | 13.9 ms                                                | 8.50 ms: 1.64x faster                                                       |
| pickle_pure_python      | 453 us                                                 | 282 us: 1.61x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 74.1 ms: 1.59x faster                                                       |
| scimark_monte_carlo     | 105 ms                                                 | 66.1 ms: 1.58x faster                                                       |
| chaos                   | 104 ms                                                 | 66.1 ms: 1.57x faster                                                       |
| hexiom                  | 9.42 ms                                                | 6.08 ms: 1.55x faster                                                       |
| spectral_norm           | 148 ms                                                 | 96.1 ms: 1.54x faster                                                       |
| deepcopy_memo           | 50.0 us                                                | 33.5 us: 1.49x faster                                                       |
| float                   | 108 ms                                                 | 72.3 ms: 1.49x faster                                                       |
| unpickle_pure_python    | 297 us                                                 | 199 us: 1.49x faster                                                        |
| scimark_lu              | 158 ms                                                 | 106 ms: 1.49x faster                                                        |
| mako                    | 14.3 ms                                                | 9.72 ms: 1.47x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.39 ms: 1.46x faster                                                       |
| nbody                   | 136 ms                                                 | 93.6 ms: 1.46x faster                                                       |
| genshi_text             | 30.6 ms                                                | 21.3 ms: 1.44x faster                                                       |
| html5lib                | 85.8 ms                                                | 59.7 ms: 1.44x faster                                                       |
| sqlglot_transpile       | 2.42 ms                                                | 1.69 ms: 1.43x faster                                                       |
| unpack_sequence         | 59.5 ns                                                | 41.6 ns: 1.43x faster                                                       |
| logging_format          | 8.92 us                                                | 6.28 us: 1.42x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.49 ms: 1.42x faster                                                       |
| pprint_pformat          | 1.97 sec                                               | 1.39 sec: 1.42x faster                                                      |
| logging_simple          | 8.06 us                                                | 5.69 us: 1.42x faster                                                       |
| django_template         | 46.3 ms                                                | 32.9 ms: 1.40x faster                                                       |
| pprint_safe_repr        | 943 ms                                                 | 677 ms: 1.39x faster                                                        |
| xml_etree_process       | 74.5 ms                                                | 53.6 ms: 1.39x faster                                                       |
| thrift                  | 1.03 ms                                                | 745 us: 1.39x faster                                                        |
| chameleon               | 8.86 ms                                                | 6.43 ms: 1.38x faster                                                       |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.03 ms: 1.36x faster                                                       |
| genshi_xml              | 63.6 ms                                                | 47.0 ms: 1.35x faster                                                       |
| async_tree_memoization  | 854 ms                                                 | 635 ms: 1.35x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.34x faster                                                      |
| pycparser               | 1.51 sec                                               | 1.13 sec: 1.34x faster                                                      |
| async_tree_none         | 713 ms                                                 | 533 ms: 1.34x faster                                                        |
| regex_compile           | 174 ms                                                 | 130 ms: 1.34x faster                                                        |
| deepcopy                | 429 us                                                 | 326 us: 1.32x faster                                                        |
| scimark_fft             | 414 ms                                                 | 315 ms: 1.31x faster                                                        |
| 2to3                    | 332 ms                                                 | 253 ms: 1.31x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                        |
| deepcopy_reduce         | 3.75 us                                                | 2.88 us: 1.30x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 50.5 ms: 1.29x faster                                                       |
| fannkuch                | 477 ms                                                 | 372 ms: 1.28x faster                                                        |
| docutils                | 3.18 sec                                               | 2.49 sec: 1.28x faster                                                      |
| coroutines              | 31.7 ms                                                | 25.0 ms: 1.27x faster                                                       |
| nqueens                 | 99.3 ms                                                | 78.5 ms: 1.26x faster                                                       |
| mypy                    | 1.01 sec                                               | 804 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 765 ms: 1.24x faster                                                        |
| bench_thread_pool       | 943 us                                                 | 774 us: 1.22x faster                                                        |
| dulwich_log             | 75.5 ms                                                | 62.0 ms: 1.22x faster                                                       |
| xml_etree_generate      | 93.3 ms                                                | 77.2 ms: 1.21x faster                                                       |
| async_generators        | 428 ms                                                 | 355 ms: 1.20x faster                                                        |
| json_loads              | 28.9 us                                                | 24.0 us: 1.20x faster                                                       |
| sympy_expand            | 537 ms                                                 | 449 ms: 1.20x faster                                                        |
| sympy_integrate         | 23.9 ms                                                | 20.2 ms: 1.19x faster                                                       |
| sympy_str               | 324 ms                                                 | 282 ms: 1.15x faster                                                        |
| sympy_sum               | 183 ms                                                 | 161 ms: 1.14x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                                       |
| sqlite_synth            | 2.90 us                                                | 2.56 us: 1.13x faster                                                       |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                       |
| json                    | 5.35 ms                                                | 4.80 ms: 1.12x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.54 sec: 1.11x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                        |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                        |
| pickle_list             | 4.50 us                                                | 4.12 us: 1.09x faster                                                       |
| telco                   | 6.68 ms                                                | 6.17 ms: 1.08x faster                                                       |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                                        |
| unpickle                | 14.3 us                                                | 13.3 us: 1.07x faster                                                       |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                                        |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                       |
| regex_dna               | 214 ms                                                 | 219 ms: 1.02x slower                                                        |
| generators              | 75.8 ms                                                | 77.6 ms: 1.02x slower                                                       |
| unpickle_list           | 4.99 us                                                | 5.12 us: 1.03x slower                                                       |
| python_startup_no_site  | 5.76 ms                                                | 6.08 ms: 1.06x slower                                                       |
| pickle_dict             | 28.3 us                                                | 30.6 us: 1.08x slower                                                       |
| regex_effbot            | 3.21 ms                                                | 3.58 ms: 1.12x slower                                                       |
| coverage                | 75.3 ms                                                | 99.4 ms: 1.32x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/mdboom/Work/builds/benchmarking/results/bm-20221217-3.12.0a3+-bcd7980/bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980.json: djangocms
