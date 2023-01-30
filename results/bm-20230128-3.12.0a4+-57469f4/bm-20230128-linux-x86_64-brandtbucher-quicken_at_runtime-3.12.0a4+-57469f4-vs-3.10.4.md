
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 57469f4
- commit date: 2023-01-28
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 254 ms: 1.31x faster                                                       |
| chameleon      | 8.86 ms                                                | 6.40 ms: 1.38x faster                                                      |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                     |
| html5lib       | 85.8 ms                                                | 61.4 ms: 1.40x faster                                                      |
| tornado_http   | 128 ms                                                 | 94.3 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                  | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 136 ms                                                 | 92.3 ms: 1.48x faster                                                      |
| float          | 108 ms                                                 | 75.1 ms: 1.43x faster                                                      |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.28x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 131 ms: 1.33x faster                                                       |
| regex_v8       | 25.0 ms                                                | 22.7 ms: 1.10x faster                                                      |
| regex_dna      | 214 ms                                                 | 219 ms: 1.03x slower                                                       |
| regex_effbot   | 3.21 ms                                                | 3.60 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 292 us: 1.55x faster                                                       |
| json_dumps           | 13.5 ms                                                | 9.40 ms: 1.43x faster                                                      |
| unpickle_pure_python | 297 us                                                 | 208 us: 1.43x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 53.6 ms: 1.39x faster                                                      |
| json_loads           | 28.9 us                                                | 23.9 us: 1.21x faster                                                      |
| xml_etree_generate   | 93.3 ms                                                | 77.5 ms: 1.20x faster                                                      |
| pickle_list          | 4.50 us                                                | 4.06 us: 1.11x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| unpickle             | 14.3 us                                                | 13.1 us: 1.09x faster                                                      |
| xml_etree_iterparse  | 110 ms                                                 | 106 ms: 1.04x faster                                                       |
| pickle               | 10.1 us                                                | 9.98 us: 1.01x faster                                                      |
| unpickle_list        | 4.99 us                                                | 5.07 us: 1.02x slower                                                      |
| pickle_dict          | 28.3 us                                                | 30.8 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.70 ms: 1.60x faster                                                      |
| python_startup_no_site | 5.76 ms                                                | 6.23 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.22x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.44 ms: 1.51x faster                                                      |
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.49x faster                                                      |
| django_template | 46.3 ms                                                | 32.4 ms: 1.43x faster                                                      |
| genshi_xml      | 63.6 ms                                                | 46.4 ms: 1.37x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.35 ms: 2.21x faster                                                      |
| logging_silent          | 173 ns                                                 | 90.2 ns: 1.92x faster                                                      |
| richards                | 71.4 ms                                                | 42.9 ms: 1.66x faster                                                      |
| raytrace                | 461 ms                                                 | 282 ms: 1.63x faster                                                       |
| scimark_sor             | 193 ms                                                 | 118 ms: 1.63x faster                                                       |
| crypto_pyaes            | 118 ms                                                 | 72.6 ms: 1.62x faster                                                      |
| go                      | 226 ms                                                 | 140 ms: 1.61x faster                                                       |
| python_startup          | 13.9 ms                                                | 8.70 ms: 1.60x faster                                                      |
| chaos                   | 104 ms                                                 | 65.9 ms: 1.58x faster                                                      |
| pyflate                 | 675 ms                                                 | 432 ms: 1.56x faster                                                       |
| scimark_monte_carlo     | 105 ms                                                 | 67.3 ms: 1.56x faster                                                      |
| pickle_pure_python      | 453 us                                                 | 292 us: 1.55x faster                                                       |
| spectral_norm           | 148 ms                                                 | 96.1 ms: 1.54x faster                                                      |
| hexiom                  | 9.42 ms                                                | 6.16 ms: 1.53x faster                                                      |
| mako                    | 14.3 ms                                                | 9.44 ms: 1.51x faster                                                      |
| scimark_lu              | 158 ms                                                 | 105 ms: 1.50x faster                                                       |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.49x faster                                                      |
| nbody                   | 136 ms                                                 | 92.3 ms: 1.48x faster                                                      |
| deepcopy_memo           | 50.0 us                                                | 34.0 us: 1.47x faster                                                      |
| json_dumps              | 13.5 ms                                                | 9.40 ms: 1.43x faster                                                      |
| float                   | 108 ms                                                 | 75.1 ms: 1.43x faster                                                      |
| django_template         | 46.3 ms                                                | 32.4 ms: 1.43x faster                                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.43 ms: 1.43x faster                                                      |
| unpickle_pure_python    | 297 us                                                 | 208 us: 1.43x faster                                                       |
| unpack_sequence         | 59.5 ns                                                | 41.7 ns: 1.43x faster                                                      |
| pprint_pformat          | 1.97 sec                                               | 1.41 sec: 1.40x faster                                                     |
| sqlglot_transpile       | 2.42 ms                                                | 1.72 ms: 1.40x faster                                                      |
| logging_format          | 8.92 us                                                | 6.37 us: 1.40x faster                                                      |
| logging_simple          | 8.06 us                                                | 5.75 us: 1.40x faster                                                      |
| html5lib                | 85.8 ms                                                | 61.4 ms: 1.40x faster                                                      |
| scimark_sparse_mat_mult | 5.48 ms                                                | 3.94 ms: 1.39x faster                                                      |
| xml_etree_process       | 74.5 ms                                                | 53.6 ms: 1.39x faster                                                      |
| thrift                  | 1.03 ms                                                | 744 us: 1.39x faster                                                       |
| pprint_safe_repr        | 943 ms                                                 | 681 ms: 1.38x faster                                                       |
| chameleon               | 8.86 ms                                                | 6.40 ms: 1.38x faster                                                      |
| scimark_fft             | 414 ms                                                 | 302 ms: 1.37x faster                                                       |
| genshi_xml              | 63.6 ms                                                | 46.4 ms: 1.37x faster                                                      |
| async_tree_none         | 713 ms                                                 | 522 ms: 1.37x faster                                                       |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.36x faster                                                     |
| tornado_http            | 128 ms                                                 | 94.3 ms: 1.36x faster                                                      |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                                      |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                      |
| regex_compile           | 174 ms                                                 | 131 ms: 1.33x faster                                                       |
| deepcopy                | 429 us                                                 | 324 us: 1.32x faster                                                       |
| 2to3                    | 332 ms                                                 | 254 ms: 1.31x faster                                                       |
| pycparser               | 1.51 sec                                               | 1.16 sec: 1.31x faster                                                     |
| async_tree_memoization  | 854 ms                                                 | 661 ms: 1.29x faster                                                       |
| deepcopy_reduce         | 3.75 us                                                | 2.91 us: 1.29x faster                                                      |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                      |
| nqueens                 | 99.3 ms                                                | 78.0 ms: 1.27x faster                                                      |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                     |
| mypy                    | 1.01 sec                                               | 807 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                                       |
| fannkuch                | 477 ms                                                 | 385 ms: 1.24x faster                                                       |
| coroutines              | 31.7 ms                                                | 26.0 ms: 1.22x faster                                                      |
| json_loads              | 28.9 us                                                | 23.9 us: 1.21x faster                                                      |
| async_generators        | 428 ms                                                 | 355 ms: 1.21x faster                                                       |
| bench_thread_pool       | 943 us                                                 | 783 us: 1.20x faster                                                       |
| xml_etree_generate      | 93.3 ms                                                | 77.5 ms: 1.20x faster                                                      |
| sympy_str               | 324 ms                                                 | 270 ms: 1.20x faster                                                       |
| dulwich_log             | 75.5 ms                                                | 62.9 ms: 1.20x faster                                                      |
| sympy_integrate         | 23.9 ms                                                | 20.0 ms: 1.20x faster                                                      |
| sympy_expand            | 537 ms                                                 | 454 ms: 1.18x faster                                                       |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                       |
| json                    | 5.35 ms                                                | 4.61 ms: 1.16x faster                                                      |
| mdp                     | 2.82 sec                                               | 2.45 sec: 1.15x faster                                                     |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                                      |
| sqlite_synth            | 2.90 us                                                | 2.59 us: 1.12x faster                                                      |
| pickle_list             | 4.50 us                                                | 4.06 us: 1.11x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| regex_v8                | 25.0 ms                                                | 22.7 ms: 1.10x faster                                                      |
| unpickle                | 14.3 us                                                | 13.1 us: 1.09x faster                                                      |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                       |
| telco                   | 6.68 ms                                                | 6.34 ms: 1.05x faster                                                      |
| xml_etree_iterparse     | 110 ms                                                 | 106 ms: 1.04x faster                                                       |
| generators              | 75.8 ms                                                | 74.4 ms: 1.02x faster                                                      |
| pickle                  | 10.1 us                                                | 9.98 us: 1.01x faster                                                      |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                       |
| unpickle_list           | 4.99 us                                                | 5.07 us: 1.02x slower                                                      |
| regex_dna               | 214 ms                                                 | 219 ms: 1.03x slower                                                       |
| python_startup_no_site  | 5.76 ms                                                | 6.23 ms: 1.08x slower                                                      |
| pickle_dict             | 28.3 us                                                | 30.8 us: 1.09x slower                                                      |
| regex_effbot            | 3.21 ms                                                | 3.60 ms: 1.12x slower                                                      |
| coverage                | 75.3 ms                                                | 102 ms: 1.35x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                               |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230128-3.12.0a4+-57469f4/bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
