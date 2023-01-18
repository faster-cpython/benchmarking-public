
# Results vs. 3.10.4

- fork: iritkatriel
- ref: copy_consts
- machine: linux-x86_64
- commit hash: f8449d5
- commit date: 2023-01-18
- overall geometric mean: 1.28x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 257 ms: 1.29x faster                                               |
| chameleon      | 8.86 ms                                                | 6.53 ms: 1.36x faster                                              |
| docutils       | 3.18 sec                                               | 2.59 sec: 1.23x faster                                             |
| html5lib       | 85.8 ms                                                | 61.5 ms: 1.39x faster                                              |
| Geometric mean | (ref)                                                  | 1.32x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 108 ms                                                 | 73.5 ms: 1.47x faster                                              |
| nbody          | 136 ms                                                 | 93.4 ms: 1.46x faster                                              |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.29x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 132 ms: 1.31x faster                                               |
| regex_dna      | 214 ms                                                 | 201 ms: 1.06x faster                                               |
| regex_effbot   | 3.21 ms                                                | 3.41 ms: 1.06x slower                                              |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.17x faster                                              |
| Geometric mean | (ref)                                                  | 1.11x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.65 ms: 1.40x faster                                              |
| json_loads           | 28.9 us                                                | 24.1 us: 1.20x faster                                              |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                              |
| pickle_dict          | 28.3 us                                                | 30.6 us: 1.08x slower                                              |
| pickle_list          | 4.50 us                                                | 4.03 us: 1.12x faster                                              |
| pickle_pure_python   | 453 us                                                 | 293 us: 1.55x faster                                               |
| unpickle             | 14.3 us                                                | 13.3 us: 1.07x faster                                              |
| unpickle_list        | 4.99 us                                                | 4.97 us: 1.00x faster                                              |
| unpickle_pure_python | 297 us                                                 | 201 us: 1.47x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                               |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.07x faster                                               |
| xml_etree_generate   | 93.3 ms                                                | 78.6 ms: 1.19x faster                                              |
| xml_etree_process    | 74.5 ms                                                | 54.6 ms: 1.36x faster                                              |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.56 ms: 1.63x faster                                              |
| python_startup_no_site | 5.76 ms                                                | 6.10 ms: 1.06x slower                                              |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 33.8 ms: 1.37x faster                                              |
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                              |
| genshi_xml      | 63.6 ms                                                | 48.1 ms: 1.32x faster                                              |
| mako            | 14.3 ms                                                | 9.67 ms: 1.47x faster                                              |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 257 ms: 1.29x faster                                               |
| async_generators        | 428 ms                                                 | 358 ms: 1.19x faster                                               |
| async_tree_none         | 713 ms                                                 | 530 ms: 1.35x faster                                               |
| async_tree_cpu_io_mixed | 949 ms                                                 | 757 ms: 1.25x faster                                               |
| async_tree_io           | 1.78 sec                                               | 1.34 sec: 1.33x faster                                             |
| async_tree_memoization  | 854 ms                                                 | 674 ms: 1.27x faster                                               |
| chameleon               | 8.86 ms                                                | 6.53 ms: 1.36x faster                                              |
| chaos                   | 104 ms                                                 | 68.6 ms: 1.52x faster                                              |
| bench_thread_pool       | 943 us                                                 | 797 us: 1.18x faster                                               |
| coroutines              | 31.7 ms                                                | 25.6 ms: 1.24x faster                                              |
| coverage                | 75.3 ms                                                | 98.3 ms: 1.30x slower                                              |
| crypto_pyaes            | 118 ms                                                 | 74.7 ms: 1.57x faster                                              |
| deepcopy                | 429 us                                                 | 341 us: 1.26x faster                                               |
| deepcopy_reduce         | 3.75 us                                                | 3.00 us: 1.25x faster                                              |
| deepcopy_memo           | 50.0 us                                                | 35.1 us: 1.43x faster                                              |
| deltablue               | 7.39 ms                                                | 3.38 ms: 2.19x faster                                              |
| django_template         | 46.3 ms                                                | 33.8 ms: 1.37x faster                                              |
| docutils                | 3.18 sec                                               | 2.59 sec: 1.23x faster                                             |
| dulwich_log             | 75.5 ms                                                | 63.4 ms: 1.19x faster                                              |
| fannkuch                | 477 ms                                                 | 367 ms: 1.30x faster                                               |
| float                   | 108 ms                                                 | 73.5 ms: 1.47x faster                                              |
| generators              | 75.8 ms                                                | 79.0 ms: 1.04x slower                                              |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                              |
| genshi_xml              | 63.6 ms                                                | 48.1 ms: 1.32x faster                                              |
| go                      | 226 ms                                                 | 139 ms: 1.63x faster                                               |
| hexiom                  | 9.42 ms                                                | 6.18 ms: 1.52x faster                                              |
| html5lib                | 85.8 ms                                                | 61.5 ms: 1.39x faster                                              |
| json                    | 5.35 ms                                                | 4.70 ms: 1.14x faster                                              |
| json_dumps              | 13.5 ms                                                | 9.65 ms: 1.40x faster                                              |
| json_loads              | 28.9 us                                                | 24.1 us: 1.20x faster                                              |
| logging_format          | 8.92 us                                                | 6.66 us: 1.34x faster                                              |
| logging_silent          | 173 ns                                                 | 95.0 ns: 1.82x faster                                              |
| logging_simple          | 8.06 us                                                | 6.06 us: 1.33x faster                                              |
| mako                    | 14.3 ms                                                | 9.67 ms: 1.47x faster                                              |
| mdp                     | 2.82 sec                                               | 2.53 sec: 1.12x faster                                             |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                               |
| mypy                    | 1.01 sec                                               | 855 ms: 1.19x faster                                               |
| nbody                   | 136 ms                                                 | 93.4 ms: 1.46x faster                                              |
| nqueens                 | 99.3 ms                                                | 81.8 ms: 1.21x faster                                              |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                              |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                              |
| pickle_dict             | 28.3 us                                                | 30.6 us: 1.08x slower                                              |
| pickle_list             | 4.50 us                                                | 4.03 us: 1.12x faster                                              |
| pickle_pure_python      | 453 us                                                 | 293 us: 1.55x faster                                               |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                               |
| pprint_safe_repr        | 943 ms                                                 | 700 ms: 1.35x faster                                               |
| pprint_pformat          | 1.97 sec                                               | 1.42 sec: 1.39x faster                                             |
| pycparser               | 1.51 sec                                               | 1.11 sec: 1.36x faster                                             |
| pyflate                 | 675 ms                                                 | 406 ms: 1.66x faster                                               |
| python_startup          | 13.9 ms                                                | 8.56 ms: 1.63x faster                                              |
| python_startup_no_site  | 5.76 ms                                                | 6.10 ms: 1.06x slower                                              |
| raytrace                | 461 ms                                                 | 293 ms: 1.58x faster                                               |
| regex_compile           | 174 ms                                                 | 132 ms: 1.31x faster                                               |
| regex_dna               | 214 ms                                                 | 201 ms: 1.06x faster                                               |
| regex_effbot            | 3.21 ms                                                | 3.41 ms: 1.06x slower                                              |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.17x faster                                              |
| richards                | 71.4 ms                                                | 43.8 ms: 1.63x faster                                              |
| scimark_fft             | 414 ms                                                 | 314 ms: 1.32x faster                                               |
| scimark_lu              | 158 ms                                                 | 111 ms: 1.42x faster                                               |
| scimark_monte_carlo     | 105 ms                                                 | 67.4 ms: 1.55x faster                                              |
| scimark_sor             | 193 ms                                                 | 108 ms: 1.80x faster                                               |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.03 ms: 1.36x faster                                              |
| spectral_norm           | 148 ms                                                 | 99.0 ms: 1.50x faster                                              |
| sqlglot_parse           | 2.04 ms                                                | 1.45 ms: 1.41x faster                                              |
| sqlglot_transpile       | 2.42 ms                                                | 1.75 ms: 1.38x faster                                              |
| sqlglot_optimize        | 65.3 ms                                                | 52.5 ms: 1.25x faster                                              |
| sqlglot_normalize       | 135 ms                                                 | 108 ms: 1.25x faster                                               |
| sqlite_synth            | 2.90 us                                                | 2.56 us: 1.13x faster                                              |
| sympy_expand            | 537 ms                                                 | 469 ms: 1.15x faster                                               |
| sympy_integrate         | 23.9 ms                                                | 21.9 ms: 1.09x faster                                              |
| sympy_sum               | 183 ms                                                 | 167 ms: 1.10x faster                                               |
| sympy_str               | 324 ms                                                 | 288 ms: 1.13x faster                                               |
| telco                   | 6.68 ms                                                | 6.31 ms: 1.06x faster                                              |
| thrift                  | 1.03 ms                                                | 749 us: 1.38x faster                                               |
| unpack_sequence         | 59.5 ns                                                | 41.6 ns: 1.43x faster                                              |
| unpickle                | 14.3 us                                                | 13.3 us: 1.07x faster                                              |
| unpickle_list           | 4.99 us                                                | 4.97 us: 1.00x faster                                              |
| unpickle_pure_python    | 297 us                                                 | 201 us: 1.47x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                               |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.07x faster                                               |
| xml_etree_generate      | 93.3 ms                                                | 78.6 ms: 1.19x faster                                              |
| xml_etree_process       | 74.5 ms                                                | 54.6 ms: 1.36x faster                                              |
| Geometric mean          | (ref)                                                  | 1.28x faster                                                       |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-f8449d5/bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
