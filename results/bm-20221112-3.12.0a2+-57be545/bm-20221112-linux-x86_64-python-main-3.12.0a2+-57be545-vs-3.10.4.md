
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 57be545
- commit date: 2022-11-12
- overall geometric mean: 1.32x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 246 ms: 1.37x faster                                   |
| chameleon      | 9.17 ms                                                | 6.49 ms: 1.41x faster                                  |
| html5lib       | 85.9 ms                                                | 58.9 ms: 1.46x faster                                  |
| tornado_http   | 128 ms                                                 | 92.5 ms: 1.39x faster                                  |
| Geometric mean | (ref)                                                  | 1.40x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.4 ms: 1.54x faster                                  |
| float          | 109 ms                                                 | 73.3 ms: 1.49x faster                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| regex_dna      | 214 ms                                                 | 205 ms: 1.04x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.64 ms: 1.14x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 281 us: 1.61x faster                                   |
| unpickle_pure_python | 302 us                                                 | 200 us: 1.51x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.44 ms: 1.42x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 53.0 ms: 1.41x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 76.8 ms: 1.22x faster                                  |
| json_loads           | 28.7 us                                                | 24.2 us: 1.19x faster                                  |
| pickle_list          | 4.72 us                                                | 4.14 us: 1.14x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.07x faster                                   |
| unpickle             | 14.2 us                                                | 13.3 us: 1.06x faster                                  |
| pickle               | 10.2 us                                                | 10.0 us: 1.01x faster                                  |
| pickle_dict          | 27.6 us                                                | 31.1 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.52 ms: 1.65x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.24 ms: 1.08x slower                                  |
| Geometric mean         | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.70 ms: 1.51x faster                                  |
| genshi_text     | 30.6 ms                                                | 21.3 ms: 1.43x faster                                  |
| django_template | 46.3 ms                                                | 32.5 ms: 1.43x faster                                  |
| genshi_xml      | 63.7 ms                                                | 46.8 ms: 1.36x faster                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.22 ms: 2.26x faster                                  |
| logging_silent          | 176 ns                                                 | 91.8 ns: 1.92x faster                                  |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.90x faster                                   |
| richards                | 75.2 ms                                                | 41.7 ms: 1.80x faster                                  |
| pyflate                 | 676 ms                                                 | 402 ms: 1.68x faster                                   |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                   |
| raytrace                | 467 ms                                                 | 281 ms: 1.66x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 65.5 ms: 1.66x faster                                  |
| python_startup          | 14.1 ms                                                | 8.52 ms: 1.65x faster                                  |
| pickle_pure_python      | 452 us                                                 | 281 us: 1.61x faster                                   |
| chaos                   | 106 ms                                                 | 67.0 ms: 1.58x faster                                  |
| spectral_norm           | 150 ms                                                 | 95.2 ms: 1.57x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 75.1 ms: 1.55x faster                                  |
| nbody                   | 144 ms                                                 | 93.4 ms: 1.54x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.13 ms: 1.54x faster                                  |
| deepcopy_memo           | 51.7 us                                                | 34.0 us: 1.52x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.35 ms: 1.52x faster                                  |
| mako                    | 14.7 ms                                                | 9.70 ms: 1.51x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 200 us: 1.51x faster                                   |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                   |
| float                   | 109 ms                                                 | 73.3 ms: 1.49x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.64 ms: 1.48x faster                                  |
| html5lib                | 85.9 ms                                                | 58.9 ms: 1.46x faster                                  |
| genshi_text             | 30.6 ms                                                | 21.3 ms: 1.43x faster                                  |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.43x faster                                  |
| json_dumps              | 13.4 ms                                                | 9.44 ms: 1.42x faster                                  |
| chameleon               | 9.17 ms                                                | 6.49 ms: 1.41x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 53.0 ms: 1.41x faster                                  |
| logging_simple          | 8.10 us                                                | 5.77 us: 1.40x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.41 sec: 1.40x faster                                 |
| logging_format          | 8.85 us                                                | 6.34 us: 1.40x faster                                  |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                   |
| thrift                  | 1.03 ms                                                | 745 us: 1.39x faster                                   |
| pprint_safe_repr        | 953 ms                                                 | 688 ms: 1.39x faster                                   |
| tornado_http            | 128 ms                                                 | 92.5 ms: 1.39x faster                                  |
| pycparser               | 1.53 sec                                               | 1.11 sec: 1.37x faster                                 |
| 2to3                    | 335 ms                                                 | 246 ms: 1.37x faster                                   |
| scimark_fft             | 421 ms                                                 | 309 ms: 1.36x faster                                   |
| genshi_xml              | 63.7 ms                                                | 46.8 ms: 1.36x faster                                  |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                 |
| async_tree_none         | 711 ms                                                 | 528 ms: 1.35x faster                                   |
| aiohttp                 | 1.34 ms                                                | 998 us: 1.34x faster                                   |
| unpack_sequence         | 59.4 ns                                                | 44.2 ns: 1.34x faster                                  |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                  |
| async_tree_memoization  | 855 ms                                                 | 646 ms: 1.32x faster                                   |
| deepcopy                | 438 us                                                 | 332 us: 1.32x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.16 ms: 1.31x faster                                  |
| coroutines              | 31.6 ms                                                | 24.1 ms: 1.31x faster                                  |
| deepcopy_reduce         | 3.79 us                                                | 2.90 us: 1.31x faster                                  |
| fannkuch                | 488 ms                                                 | 374 ms: 1.31x faster                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 731 ms: 1.30x faster                                   |
| sqlglot_optimize        | 65.2 ms                                                | 50.5 ms: 1.29x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.29x faster                                   |
| dulwich_log             | 75.8 ms                                                | 61.1 ms: 1.24x faster                                  |
| nqueens                 | 100 ms                                                 | 81.1 ms: 1.23x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 76.8 ms: 1.22x faster                                  |
| json_loads              | 28.7 us                                                | 24.2 us: 1.19x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.18x faster                                  |
| sympy_expand            | 534 ms                                                 | 458 ms: 1.16x faster                                   |
| sympy_str               | 325 ms                                                 | 283 ms: 1.15x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.14x faster                                  |
| pickle_list             | 4.72 us                                                | 4.14 us: 1.14x faster                                  |
| json                    | 5.35 ms                                                | 4.71 ms: 1.14x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| sympy_sum               | 183 ms                                                 | 164 ms: 1.12x faster                                   |
| mdp                     | 2.74 sec                                               | 2.47 sec: 1.11x faster                                 |
| sqlite_synth            | 2.92 us                                                | 2.65 us: 1.11x faster                                  |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.07x faster                                   |
| telco                   | 6.73 ms                                                | 6.32 ms: 1.07x faster                                  |
| unpickle                | 14.2 us                                                | 13.3 us: 1.06x faster                                  |
| regex_dna               | 214 ms                                                 | 205 ms: 1.04x faster                                   |
| pickle                  | 10.2 us                                                | 10.0 us: 1.01x faster                                  |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| generators              | 76.4 ms                                                | 79.6 ms: 1.04x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.24 ms: 1.08x slower                                  |
| pickle_dict             | 27.6 us                                                | 31.1 us: 1.13x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.64 ms: 1.14x slower                                  |
| coverage                | 74.7 ms                                                | 99.8 ms: 1.34x slower                                  |
| Geometric mean          | (ref)                                                  | 1.32x faster                                           |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: async_generators, asyncio_tcp, bench_mp_pool, bench_thread_pool, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221112-3.12.0a2+-57be545/bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545.json: mypy
