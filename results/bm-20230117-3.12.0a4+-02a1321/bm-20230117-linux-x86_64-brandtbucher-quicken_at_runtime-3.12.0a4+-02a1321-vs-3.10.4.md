
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 02a1321
- commit date: 2023-01-17
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 256 ms: 1.30x faster                                                       |
| chameleon      | 8.86 ms                                                | 6.32 ms: 1.40x faster                                                      |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                     |
| html5lib       | 85.8 ms                                                | 61.5 ms: 1.39x faster                                                      |
| tornado_http   | 128 ms                                                 | 94.4 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                  | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 136 ms                                                 | 94.0 ms: 1.45x faster                                                      |
| float          | 108 ms                                                 | 76.0 ms: 1.42x faster                                                      |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.27x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 130 ms: 1.34x faster                                                       |
| regex_v8       | 25.0 ms                                                | 21.5 ms: 1.16x faster                                                      |
| regex_dna      | 214 ms                                                 | 209 ms: 1.03x faster                                                       |
| regex_effbot   | 3.21 ms                                                | 3.65 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 293 us: 1.55x faster                                                       |
| json_dumps           | 13.5 ms                                                | 9.34 ms: 1.44x faster                                                      |
| unpickle_pure_python | 297 us                                                 | 209 us: 1.42x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                      |
| xml_etree_generate   | 93.3 ms                                                | 76.9 ms: 1.21x faster                                                      |
| json_loads           | 28.9 us                                                | 23.9 us: 1.21x faster                                                      |
| pickle_list          | 4.50 us                                                | 4.08 us: 1.10x faster                                                      |
| unpickle             | 14.3 us                                                | 13.0 us: 1.10x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 151 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                 | 105 ms: 1.05x faster                                                       |
| unpickle_list        | 4.99 us                                                | 4.93 us: 1.01x faster                                                      |
| pickle               | 10.1 us                                                | 10.1 us: 1.01x faster                                                      |
| pickle_dict          | 28.3 us                                                | 30.8 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.74 ms: 1.59x faster                                                      |
| python_startup_no_site | 5.76 ms                                                | 6.27 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.21x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.2 ms: 1.52x faster                                                      |
| mako            | 14.3 ms                                                | 9.71 ms: 1.47x faster                                                      |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                      |
| genshi_xml      | 63.6 ms                                                | 46.2 ms: 1.38x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.50 ms: 2.11x faster                                                      |
| logging_silent          | 173 ns                                                 | 89.6 ns: 1.93x faster                                                      |
| go                      | 226 ms                                                 | 139 ms: 1.63x faster                                                       |
| crypto_pyaes            | 118 ms                                                 | 72.0 ms: 1.63x faster                                                      |
| scimark_sor             | 193 ms                                                 | 119 ms: 1.62x faster                                                       |
| chaos                   | 104 ms                                                 | 64.7 ms: 1.61x faster                                                      |
| pyflate                 | 675 ms                                                 | 420 ms: 1.61x faster                                                       |
| python_startup          | 13.9 ms                                                | 8.74 ms: 1.59x faster                                                      |
| hexiom                  | 9.42 ms                                                | 6.00 ms: 1.57x faster                                                      |
| pickle_pure_python      | 453 us                                                 | 293 us: 1.55x faster                                                       |
| raytrace                | 461 ms                                                 | 299 ms: 1.54x faster                                                       |
| richards                | 71.4 ms                                                | 46.6 ms: 1.53x faster                                                      |
| spectral_norm           | 148 ms                                                 | 97.5 ms: 1.52x faster                                                      |
| genshi_text             | 30.6 ms                                                | 20.2 ms: 1.52x faster                                                      |
| scimark_monte_carlo     | 105 ms                                                 | 69.8 ms: 1.50x faster                                                      |
| scimark_lu              | 158 ms                                                 | 107 ms: 1.49x faster                                                       |
| deepcopy_memo           | 50.0 us                                                | 34.1 us: 1.47x faster                                                      |
| mako                    | 14.3 ms                                                | 9.71 ms: 1.47x faster                                                      |
| nbody                   | 136 ms                                                 | 94.0 ms: 1.45x faster                                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                                      |
| json_dumps              | 13.5 ms                                                | 9.34 ms: 1.44x faster                                                      |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                                     |
| unpickle_pure_python    | 297 us                                                 | 209 us: 1.42x faster                                                       |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                      |
| float                   | 108 ms                                                 | 76.0 ms: 1.42x faster                                                      |
| sqlglot_transpile       | 2.42 ms                                                | 1.71 ms: 1.41x faster                                                      |
| pprint_safe_repr        | 943 ms                                                 | 670 ms: 1.41x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                      |
| chameleon               | 8.86 ms                                                | 6.32 ms: 1.40x faster                                                      |
| thrift                  | 1.03 ms                                                | 738 us: 1.40x faster                                                       |
| html5lib                | 85.8 ms                                                | 61.5 ms: 1.39x faster                                                      |
| logging_simple          | 8.06 us                                                | 5.81 us: 1.39x faster                                                      |
| logging_format          | 8.92 us                                                | 6.45 us: 1.38x faster                                                      |
| genshi_xml              | 63.6 ms                                                | 46.2 ms: 1.38x faster                                                      |
| unpack_sequence         | 59.5 ns                                                | 43.5 ns: 1.37x faster                                                      |
| async_tree_none         | 713 ms                                                 | 522 ms: 1.36x faster                                                       |
| tornado_http            | 128 ms                                                 | 94.4 ms: 1.36x faster                                                      |
| pycparser               | 1.51 sec                                               | 1.11 sec: 1.36x faster                                                     |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                                     |
| regex_compile           | 174 ms                                                 | 130 ms: 1.34x faster                                                       |
| async_tree_memoization  | 854 ms                                                 | 637 ms: 1.34x faster                                                       |
| aiohttp                 | 1.34 ms                                                | 998 us: 1.34x faster                                                       |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                      |
| scimark_fft             | 414 ms                                                 | 310 ms: 1.33x faster                                                       |
| deepcopy                | 429 us                                                 | 326 us: 1.32x faster                                                       |
| 2to3                    | 332 ms                                                 | 256 ms: 1.30x faster                                                       |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.26 ms: 1.29x faster                                                      |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 51.1 ms: 1.28x faster                                                      |
| nqueens                 | 99.3 ms                                                | 78.0 ms: 1.27x faster                                                      |
| deepcopy_reduce         | 3.75 us                                                | 2.95 us: 1.27x faster                                                      |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                     |
| mypy                    | 1.01 sec                                               | 810 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed | 949 ms                                                 | 763 ms: 1.24x faster                                                       |
| fannkuch                | 477 ms                                                 | 385 ms: 1.24x faster                                                       |
| coroutines              | 31.7 ms                                                | 25.6 ms: 1.24x faster                                                      |
| async_generators        | 428 ms                                                 | 350 ms: 1.22x faster                                                       |
| xml_etree_generate      | 93.3 ms                                                | 76.9 ms: 1.21x faster                                                      |
| dulwich_log             | 75.5 ms                                                | 62.4 ms: 1.21x faster                                                      |
| json_loads              | 28.9 us                                                | 23.9 us: 1.21x faster                                                      |
| bench_thread_pool       | 943 us                                                 | 782 us: 1.21x faster                                                       |
| sympy_integrate         | 23.9 ms                                                | 20.0 ms: 1.20x faster                                                      |
| sympy_str               | 324 ms                                                 | 271 ms: 1.20x faster                                                       |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                       |
| sympy_expand            | 537 ms                                                 | 455 ms: 1.18x faster                                                       |
| json                    | 5.35 ms                                                | 4.56 ms: 1.18x faster                                                      |
| regex_v8                | 25.0 ms                                                | 21.5 ms: 1.16x faster                                                      |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                      |
| sqlite_synth            | 2.90 us                                                | 2.59 us: 1.12x faster                                                      |
| pickle_list             | 4.50 us                                                | 4.08 us: 1.10x faster                                                      |
| unpickle                | 14.3 us                                                | 13.0 us: 1.10x faster                                                      |
| mdp                     | 2.82 sec                                               | 2.61 sec: 1.08x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 151 ms: 1.08x faster                                                       |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.07x faster                                                       |
| telco                   | 6.68 ms                                                | 6.34 ms: 1.05x faster                                                      |
| xml_etree_iterparse     | 110 ms                                                 | 105 ms: 1.05x faster                                                       |
| regex_dna               | 214 ms                                                 | 209 ms: 1.03x faster                                                       |
| unpickle_list           | 4.99 us                                                | 4.93 us: 1.01x faster                                                      |
| pickle                  | 10.1 us                                                | 10.1 us: 1.01x faster                                                      |
| generators              | 75.8 ms                                                | 75.2 ms: 1.01x faster                                                      |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                       |
| python_startup_no_site  | 5.76 ms                                                | 6.27 ms: 1.09x slower                                                      |
| pickle_dict             | 28.3 us                                                | 30.8 us: 1.09x slower                                                      |
| regex_effbot            | 3.21 ms                                                | 3.65 ms: 1.14x slower                                                      |
| coverage                | 75.3 ms                                                | 96.7 ms: 1.28x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                               |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230117-3.12.0a4+-02a1321/bm-20230117-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-02a1321.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
