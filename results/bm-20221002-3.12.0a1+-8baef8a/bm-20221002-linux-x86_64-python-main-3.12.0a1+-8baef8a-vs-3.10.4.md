
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
| 2to3           | 332 ms                                                 | 246 ms: 1.35x faster                                   |
| chameleon      | 8.86 ms                                                | 6.38 ms: 1.39x faster                                  |
| html5lib       | 85.8 ms                                                | 59.3 ms: 1.45x faster                                  |
| tornado_http   | 128 ms                                                 | 92.8 ms: 1.38x faster                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 108 ms                                                 | 72.0 ms: 1.50x faster                                  |
| nbody          | 136 ms                                                 | 96.2 ms: 1.42x faster                                  |
| pidigits       | 190 ms                                                 | 193 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 127 ms: 1.37x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.17x faster                                  |
| regex_dna      | 214 ms                                                 | 204 ms: 1.05x faster                                   |
| regex_effbot   | 3.21 ms                                                | 3.32 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 285 us: 1.59x faster                                   |
| unpickle_pure_python | 297 us                                                 | 201 us: 1.47x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.56 ms: 1.41x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 52.9 ms: 1.41x faster                                  |
| xml_etree_generate   | 93.3 ms                                                | 75.3 ms: 1.24x faster                                  |
| json_loads           | 28.9 us                                                | 24.0 us: 1.20x faster                                  |
| pickle_list          | 4.50 us                                                | 4.06 us: 1.11x faster                                  |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.08x faster                                   |
| unpickle             | 14.3 us                                                | 13.5 us: 1.06x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 157 ms: 1.04x faster                                   |
| pickle               | 10.1 us                                                | 10.1 us: 1.01x faster                                  |
| unpickle_list        | 4.99 us                                                | 4.96 us: 1.01x faster                                  |
| pickle_dict          | 28.3 us                                                | 30.9 us: 1.09x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.35 ms: 1.67x faster                                  |
| python_startup_no_site | 5.76 ms                                                | 6.05 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.26x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.35 ms: 1.53x faster                                  |
| genshi_text     | 30.6 ms                                                | 20.7 ms: 1.48x faster                                  |
| django_template | 46.3 ms                                                | 32.4 ms: 1.43x faster                                  |
| genshi_xml      | 63.6 ms                                                | 48.4 ms: 1.31x faster                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.26 ms: 2.27x faster                                  |
| logging_silent          | 173 ns                                                 | 92.6 ns: 1.87x faster                                  |
| scimark_sor             | 193 ms                                                 | 105 ms: 1.85x faster                                   |
| go                      | 226 ms                                                 | 132 ms: 1.72x faster                                   |
| pyflate                 | 675 ms                                                 | 400 ms: 1.69x faster                                   |
| python_startup          | 13.9 ms                                                | 8.35 ms: 1.67x faster                                  |
| raytrace                | 461 ms                                                 | 278 ms: 1.66x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 72.8 ms: 1.61x faster                                  |
| richards                | 71.4 ms                                                | 44.2 ms: 1.61x faster                                  |
| spectral_norm           | 148 ms                                                 | 92.3 ms: 1.60x faster                                  |
| scimark_monte_carlo     | 105 ms                                                 | 65.6 ms: 1.60x faster                                  |
| mypy                    | 1.01 sec                                               | 635 ms: 1.60x faster                                   |
| pickle_pure_python      | 453 us                                                 | 285 us: 1.59x faster                                   |
| hexiom                  | 9.42 ms                                                | 6.00 ms: 1.57x faster                                  |
| chaos                   | 104 ms                                                 | 66.4 ms: 1.57x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.32 ms: 1.54x faster                                  |
| mako                    | 14.3 ms                                                | 9.35 ms: 1.53x faster                                  |
| sqlglot_transpile       | 2.42 ms                                                | 1.61 ms: 1.50x faster                                  |
| float                   | 108 ms                                                 | 72.0 ms: 1.50x faster                                  |
| deepcopy_memo           | 50.0 us                                                | 33.6 us: 1.49x faster                                  |
| genshi_text             | 30.6 ms                                                | 20.7 ms: 1.48x faster                                  |
| unpickle_pure_python    | 297 us                                                 | 201 us: 1.47x faster                                   |
| scimark_lu              | 158 ms                                                 | 108 ms: 1.46x faster                                   |
| html5lib                | 85.8 ms                                                | 59.3 ms: 1.45x faster                                  |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                 |
| django_template         | 46.3 ms                                                | 32.4 ms: 1.43x faster                                  |
| nbody                   | 136 ms                                                 | 96.2 ms: 1.42x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.56 ms: 1.41x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 52.9 ms: 1.41x faster                                  |
| pprint_safe_repr        | 943 ms                                                 | 670 ms: 1.41x faster                                   |
| logging_simple          | 8.06 us                                                | 5.75 us: 1.40x faster                                  |
| logging_format          | 8.92 us                                                | 6.39 us: 1.40x faster                                  |
| async_tree_none         | 713 ms                                                 | 512 ms: 1.39x faster                                   |
| chameleon               | 8.86 ms                                                | 6.38 ms: 1.39x faster                                  |
| thrift                  | 1.03 ms                                                | 744 us: 1.39x faster                                   |
| tornado_http            | 128 ms                                                 | 92.8 ms: 1.38x faster                                  |
| regex_compile           | 174 ms                                                 | 127 ms: 1.37x faster                                   |
| unpack_sequence         | 59.5 ns                                                | 43.5 ns: 1.37x faster                                  |
| pycparser               | 1.51 sec                                               | 1.10 sec: 1.37x faster                                 |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.36x faster                                 |
| 2to3                    | 332 ms                                                 | 246 ms: 1.35x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 640 ms: 1.33x faster                                   |
| coroutines              | 31.7 ms                                                | 23.9 ms: 1.33x faster                                  |
| deepcopy                | 429 us                                                 | 324 us: 1.32x faster                                   |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.32x faster                                  |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.32x faster                                  |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.17 ms: 1.32x faster                                  |
| genshi_xml              | 63.6 ms                                                | 48.4 ms: 1.31x faster                                  |
| deepcopy_reduce         | 3.75 us                                                | 2.86 us: 1.31x faster                                  |
| scimark_fft             | 414 ms                                                 | 317 ms: 1.31x faster                                   |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 730 ms: 1.30x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.6 ms: 1.29x faster                                  |
| fannkuch                | 477 ms                                                 | 371 ms: 1.29x faster                                   |
| nqueens                 | 99.3 ms                                                | 79.3 ms: 1.25x faster                                  |
| xml_etree_generate      | 93.3 ms                                                | 75.3 ms: 1.24x faster                                  |
| dulwich_log             | 75.5 ms                                                | 61.3 ms: 1.23x faster                                  |
| json_loads              | 28.9 us                                                | 24.0 us: 1.20x faster                                  |
| json                    | 5.35 ms                                                | 4.51 ms: 1.19x faster                                  |
| sympy_expand            | 537 ms                                                 | 453 ms: 1.18x faster                                   |
| sympy_integrate         | 23.9 ms                                                | 20.3 ms: 1.18x faster                                  |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.17x faster                                  |
| pylint                  | 519 ms                                                 | 447 ms: 1.16x faster                                   |
| mdp                     | 2.82 sec                                               | 2.45 sec: 1.15x faster                                 |
| sympy_str               | 324 ms                                                 | 281 ms: 1.15x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                  |
| sqlite_synth            | 2.90 us                                                | 2.57 us: 1.13x faster                                  |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.12x faster                                   |
| meteor_contest          | 114 ms                                                 | 102 ms: 1.11x faster                                   |
| pickle_list             | 4.50 us                                                | 4.06 us: 1.11x faster                                  |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.08x faster                                   |
| telco                   | 6.68 ms                                                | 6.33 ms: 1.06x faster                                  |
| unpickle                | 14.3 us                                                | 13.5 us: 1.06x faster                                  |
| generators              | 75.8 ms                                                | 72.1 ms: 1.05x faster                                  |
| regex_dna               | 214 ms                                                 | 204 ms: 1.05x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 157 ms: 1.04x faster                                   |
| pickle                  | 10.1 us                                                | 10.1 us: 1.01x faster                                  |
| unpickle_list           | 4.99 us                                                | 4.96 us: 1.01x faster                                  |
| pidigits                | 190 ms                                                 | 193 ms: 1.02x slower                                   |
| regex_effbot            | 3.21 ms                                                | 3.32 ms: 1.03x slower                                  |
| python_startup_no_site  | 5.76 ms                                                | 6.05 ms: 1.05x slower                                  |
| pickle_dict             | 28.3 us                                                | 30.9 us: 1.09x slower                                  |
| coverage                | 75.3 ms                                                | 96.6 ms: 1.28x slower                                  |
| Geometric mean          | (ref)                                                  | 1.32x faster                                           |
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: async_generators, bench_mp_pool, bench_thread_pool, docutils, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
