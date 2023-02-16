
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 8baef8a
- commit date: 2022-10-02
- overall geometric mean: 1.32x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 246 ms: 1.36x faster                                   |
| chameleon      | 9.17 ms                                                | 6.38 ms: 1.44x faster                                  |
| html5lib       | 85.9 ms                                                | 59.3 ms: 1.45x faster                                  |
| tornado_http   | 128 ms                                                 | 92.8 ms: 1.38x faster                                  |
| Geometric mean | (ref)                                                  | 1.41x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 109 ms                                                 | 72.0 ms: 1.51x faster                                  |
| nbody          | 144 ms                                                 | 96.2 ms: 1.50x faster                                  |
| pidigits       | 190 ms                                                 | 193 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.40x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.17x faster                                  |
| regex_dna      | 214 ms                                                 | 204 ms: 1.05x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.32 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 285 us: 1.59x faster                                   |
| unpickle_pure_python | 302 us                                                 | 201 us: 1.50x faster                                   |
| xml_etree_process    | 74.5 ms                                                | 52.9 ms: 1.41x faster                                  |
| json_dumps           | 13.4 ms                                                | 9.56 ms: 1.41x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 75.3 ms: 1.25x faster                                  |
| json_loads           | 28.7 us                                                | 24.0 us: 1.20x faster                                  |
| pickle_list          | 4.72 us                                                | 4.06 us: 1.16x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| unpickle             | 14.2 us                                                | 13.5 us: 1.05x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 157 ms: 1.04x faster                                   |
| pickle               | 10.2 us                                                | 10.1 us: 1.01x faster                                  |
| unpickle_list        | 4.92 us                                                | 4.96 us: 1.01x slower                                  |
| pickle_dict          | 27.6 us                                                | 30.9 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.35 ms: 1.69x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.05 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.35 ms: 1.57x faster                                  |
| genshi_text     | 30.6 ms                                                | 20.7 ms: 1.48x faster                                  |
| django_template | 46.3 ms                                                | 32.4 ms: 1.43x faster                                  |
| genshi_xml      | 63.7 ms                                                | 48.4 ms: 1.32x faster                                  |
| Geometric mean  | (ref)                                                  | 1.45x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.26 ms: 2.23x faster                                  |
| logging_silent          | 176 ns                                                 | 92.6 ns: 1.91x faster                                  |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.88x faster                                   |
| go                      | 226 ms                                                 | 132 ms: 1.71x faster                                   |
| richards                | 75.2 ms                                                | 44.2 ms: 1.70x faster                                  |
| python_startup          | 14.1 ms                                                | 8.35 ms: 1.69x faster                                  |
| pyflate                 | 676 ms                                                 | 400 ms: 1.69x faster                                   |
| raytrace                | 467 ms                                                 | 278 ms: 1.68x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 65.6 ms: 1.66x faster                                  |
| spectral_norm           | 150 ms                                                 | 92.3 ms: 1.62x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 72.8 ms: 1.60x faster                                  |
| chaos                   | 106 ms                                                 | 66.4 ms: 1.59x faster                                  |
| pickle_pure_python      | 452 us                                                 | 285 us: 1.59x faster                                   |
| hexiom                  | 9.43 ms                                                | 6.00 ms: 1.57x faster                                  |
| mako                    | 14.7 ms                                                | 9.35 ms: 1.57x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.32 ms: 1.54x faster                                  |
| deepcopy_memo           | 51.7 us                                                | 33.6 us: 1.54x faster                                  |
| float                   | 109 ms                                                 | 72.0 ms: 1.51x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.61 ms: 1.50x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 201 us: 1.50x faster                                   |
| nbody                   | 144 ms                                                 | 96.2 ms: 1.50x faster                                  |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                   |
| genshi_text             | 30.6 ms                                                | 20.7 ms: 1.48x faster                                  |
| html5lib                | 85.9 ms                                                | 59.3 ms: 1.45x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.44x faster                                 |
| chameleon               | 9.17 ms                                                | 6.38 ms: 1.44x faster                                  |
| django_template         | 46.3 ms                                                | 32.4 ms: 1.43x faster                                  |
| pprint_safe_repr        | 953 ms                                                 | 670 ms: 1.42x faster                                   |
| xml_etree_process       | 74.5 ms                                                | 52.9 ms: 1.41x faster                                  |
| logging_simple          | 8.10 us                                                | 5.75 us: 1.41x faster                                  |
| json_dumps              | 13.4 ms                                                | 9.56 ms: 1.41x faster                                  |
| regex_compile           | 177 ms                                                 | 127 ms: 1.40x faster                                   |
| thrift                  | 1.03 ms                                                | 744 us: 1.39x faster                                   |
| async_tree_none         | 711 ms                                                 | 512 ms: 1.39x faster                                   |
| logging_format          | 8.85 us                                                | 6.39 us: 1.39x faster                                  |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                 |
| tornado_http            | 128 ms                                                 | 92.8 ms: 1.38x faster                                  |
| unpack_sequence         | 59.4 ns                                                | 43.5 ns: 1.37x faster                                  |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                 |
| 2to3                    | 335 ms                                                 | 246 ms: 1.36x faster                                   |
| deepcopy                | 438 us                                                 | 324 us: 1.35x faster                                   |
| async_tree_memoization  | 855 ms                                                 | 640 ms: 1.34x faster                                   |
| scimark_fft             | 421 ms                                                 | 317 ms: 1.33x faster                                   |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                  |
| coroutines              | 31.6 ms                                                | 23.9 ms: 1.32x faster                                  |
| deepcopy_reduce         | 3.79 us                                                | 2.86 us: 1.32x faster                                  |
| genshi_xml              | 63.7 ms                                                | 48.4 ms: 1.32x faster                                  |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.32x faster                                  |
| fannkuch                | 488 ms                                                 | 371 ms: 1.31x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.17 ms: 1.31x faster                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 730 ms: 1.30x faster                                   |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.30x faster                                   |
| sqlglot_optimize        | 65.2 ms                                                | 50.6 ms: 1.29x faster                                  |
| nqueens                 | 100 ms                                                 | 79.3 ms: 1.26x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 75.3 ms: 1.25x faster                                  |
| dulwich_log             | 75.8 ms                                                | 61.3 ms: 1.24x faster                                  |
| json_loads              | 28.7 us                                                | 24.0 us: 1.20x faster                                  |
| pylint                  | 532 ms                                                 | 447 ms: 1.19x faster                                   |
| json                    | 5.35 ms                                                | 4.51 ms: 1.19x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.18x faster                                  |
| sympy_expand            | 534 ms                                                 | 453 ms: 1.18x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.17x faster                                  |
| pickle_list             | 4.72 us                                                | 4.06 us: 1.16x faster                                  |
| sympy_str               | 325 ms                                                 | 281 ms: 1.15x faster                                   |
| sqlite_synth            | 2.92 us                                                | 2.57 us: 1.14x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                  |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.12x faster                                   |
| mdp                     | 2.74 sec                                               | 2.45 sec: 1.12x faster                                 |
| meteor_contest          | 114 ms                                                 | 102 ms: 1.12x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| telco                   | 6.73 ms                                                | 6.33 ms: 1.06x faster                                  |
| generators              | 76.4 ms                                                | 72.1 ms: 1.06x faster                                  |
| unpickle                | 14.2 us                                                | 13.5 us: 1.05x faster                                  |
| regex_dna               | 214 ms                                                 | 204 ms: 1.05x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 157 ms: 1.04x faster                                   |
| pickle                  | 10.2 us                                                | 10.1 us: 1.01x faster                                  |
| unpickle_list           | 4.92 us                                                | 4.96 us: 1.01x slower                                  |
| pidigits                | 190 ms                                                 | 193 ms: 1.02x slower                                   |
| regex_effbot            | 3.19 ms                                                | 3.32 ms: 1.04x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.05 ms: 1.05x slower                                  |
| pickle_dict             | 27.6 us                                                | 30.9 us: 1.12x slower                                  |
| coverage                | 74.7 ms                                                | 96.6 ms: 1.29x slower                                  |
| Geometric mean          | (ref)                                                  | 1.32x faster                                           |
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: async_generators, asyncio_tcp, bench_mp_pool, bench_thread_pool, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221002-3.12.0a1+-8baef8a/bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a.json: mypy
