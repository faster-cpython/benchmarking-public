Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 222 ms                                                 | 184 ms: 1.21x faster                                   |
| chameleon      | 5.86 ms                                                | 4.29 ms: 1.37x faster                                  |
| docutils       | 1.76 sec                                               | 1.44 sec: 1.23x faster                                 |
| html5lib       | 44.0 ms                                                | 33.2 ms: 1.33x faster                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 72.1 ms                                                | 53.4 ms: 1.35x faster                                  |
| nbody          | 94.6 ms                                                | 62.3 ms: 1.52x faster                                  |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.2 ms                                                | 72.7 ms: 1.32x faster                                  |
| regex_dna      | 164 ms                                                 | 149 ms: 1.10x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.71 ms: 1.11x slower                                  |
| regex_v8       | 17.7 ms                                                | 16.0 ms: 1.11x faster                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 8.34 ms                                                | 6.16 ms: 1.35x faster                                  |
| json_loads           | 17.0 us                                                | 16.3 us: 1.04x faster                                  |
| pickle               | 7.50 us                                                | 7.55 us: 1.01x slower                                  |
| pickle_dict          | 18.0 us                                                | 18.0 us: 1.00x slower                                  |
| pickle_list          | 2.83 us                                                | 2.84 us: 1.01x slower                                  |
| pickle_pure_python   | 284 us                                                 | 197 us: 1.44x faster                                   |
| unpickle             | 10.0 us                                                | 9.84 us: 1.02x faster                                  |
| unpickle_list        | 2.66 us                                                | 2.56 us: 1.04x faster                                  |
| unpickle_pure_python | 204 us                                                 | 151 us: 1.35x faster                                   |
| xml_etree_parse      | 100 ms                                                 | 92.9 ms: 1.08x faster                                  |
| xml_etree_iterparse  | 69.0 ms                                                | 65.5 ms: 1.05x faster                                  |
| xml_etree_generate   | 54.5 ms                                                | 47.0 ms: 1.16x faster                                  |
| xml_etree_process    | 45.1 ms                                                | 34.4 ms: 1.31x faster                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 9.59 ms                                                | 9.29 ms: 1.03x faster                                  |
| python_startup_no_site | 7.00 ms                                                | 7.34 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 27.2 ms                                                | 20.7 ms: 1.32x faster                                  |
| genshi_text     | 18.2 ms                                                | 13.9 ms: 1.31x faster                                  |
| genshi_xml      | 37.7 ms                                                | 28.2 ms: 1.34x faster                                  |
| mako            | 10.6 ms                                                | 6.96 ms: 1.52x faster                                  |
| Geometric mean  | (ref)                                                  | 1.37x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3                    | 222 ms                                                 | 184 ms: 1.21x faster                                   |
| async_generators        | 231 ms                                                 | 201 ms: 1.15x faster                                   |
| async_tree_none         | 396 ms                                                 | 285 ms: 1.39x faster                                   |
| async_tree_cpu_io_mixed | 665 ms                                                 | 538 ms: 1.24x faster                                   |
| async_tree_io           | 1.01 sec                                               | 732 ms: 1.38x faster                                   |
| async_tree_memoization  | 485 ms                                                 | 330 ms: 1.47x faster                                   |
| chameleon               | 5.86 ms                                                | 4.29 ms: 1.37x faster                                  |
| chaos                   | 66.5 ms                                                | 48.6 ms: 1.37x faster                                  |
| bench_mp_pool           | 40.8 ms                                                | 43.9 ms: 1.08x slower                                  |
| bench_thread_pool       | 531 us                                                 | 445 us: 1.19x faster                                   |
| coroutines              | 20.1 ms                                                | 17.4 ms: 1.15x faster                                  |
| coverage                | 40.8 ms                                                | 54.9 ms: 1.35x slower                                  |
| crypto_pyaes            | 77.9 ms                                                | 53.0 ms: 1.47x faster                                  |
| deepcopy                | 278 us                                                 | 227 us: 1.22x faster                                   |
| deepcopy_reduce         | 2.36 us                                                | 1.95 us: 1.21x faster                                  |
| deepcopy_memo           | 34.4 us                                                | 27.4 us: 1.26x faster                                  |
| deltablue               | 5.37 ms                                                | 2.51 ms: 2.14x faster                                  |
| django_template         | 27.2 ms                                                | 20.7 ms: 1.32x faster                                  |
| docutils                | 1.76 sec                                               | 1.44 sec: 1.23x faster                                 |
| dulwich_log             | 36.4 ms                                                | 28.4 ms: 1.28x faster                                  |
| fannkuch                | 318 ms                                                 | 255 ms: 1.25x faster                                   |
| float                   | 72.1 ms                                                | 53.4 ms: 1.35x faster                                  |
| generators              | 32.5 ms                                                | 32.2 ms: 1.01x faster                                  |
| genshi_text             | 18.2 ms                                                | 13.9 ms: 1.31x faster                                  |
| genshi_xml              | 37.7 ms                                                | 28.2 ms: 1.34x faster                                  |
| go                      | 165 ms                                                 | 106 ms: 1.55x faster                                   |
| hexiom                  | 6.31 ms                                                | 4.59 ms: 1.37x faster                                  |
| html5lib                | 44.0 ms                                                | 33.2 ms: 1.33x faster                                  |
| json                    | 3.13 ms                                                | 2.82 ms: 1.11x faster                                  |
| json_dumps              | 8.34 ms                                                | 6.16 ms: 1.35x faster                                  |
| json_loads              | 17.0 us                                                | 16.3 us: 1.04x faster                                  |
| logging_format          | 4.95 us                                                | 3.74 us: 1.32x faster                                  |
| logging_silent          | 119 ns                                                 | 62.7 ns: 1.90x faster                                  |
| logging_simple          | 4.61 us                                                | 3.44 us: 1.34x faster                                  |
| mako                    | 10.6 ms                                                | 6.96 ms: 1.52x faster                                  |
| mdp                     | 1.66 sec                                               | 1.50 sec: 1.11x faster                                 |
| meteor_contest          | 77.7 ms                                                | 75.4 ms: 1.03x faster                                  |
| mypy                    | 521 ms                                                 | 410 ms: 1.27x faster                                   |
| nbody                   | 94.6 ms                                                | 62.3 ms: 1.52x faster                                  |
| nqueens                 | 68.6 ms                                                | 59.3 ms: 1.16x faster                                  |
| pathlib                 | 22.2 ms                                                | 20.4 ms: 1.09x faster                                  |
| pickle                  | 7.50 us                                                | 7.55 us: 1.01x slower                                  |
| pickle_dict             | 18.0 us                                                | 18.0 us: 1.00x slower                                  |
| pickle_list             | 2.83 us                                                | 2.84 us: 1.01x slower                                  |
| pickle_pure_python      | 284 us                                                 | 197 us: 1.44x faster                                   |
| pidigits                | 284 ms                                                 | 282 ms: 1.01x faster                                   |
| pprint_safe_repr        | 608 ms                                                 | 470 ms: 1.29x faster                                   |
| pprint_pformat          | 1.24 sec                                               | 955 ms: 1.30x faster                                   |
| pycparser               | 915 ms                                                 | 665 ms: 1.37x faster                                   |
| pyflate                 | 454 ms                                                 | 324 ms: 1.40x faster                                   |
| python_startup          | 9.59 ms                                                | 9.29 ms: 1.03x faster                                  |
| python_startup_no_site  | 7.00 ms                                                | 7.34 ms: 1.05x slower                                  |
| raytrace                | 329 ms                                                 | 203 ms: 1.62x faster                                   |
| regex_compile           | 96.2 ms                                                | 72.7 ms: 1.32x faster                                  |
| regex_dna               | 164 ms                                                 | 149 ms: 1.10x faster                                   |
| regex_effbot            | 2.45 ms                                                | 2.71 ms: 1.11x slower                                  |
| regex_v8                | 17.7 ms                                                | 16.0 ms: 1.11x faster                                  |
| richards                | 51.4 ms                                                | 29.2 ms: 1.76x faster                                  |
| scimark_fft             | 231 ms                                                 | 193 ms: 1.20x faster                                   |
| scimark_lu              | 110 ms                                                 | 69.0 ms: 1.59x faster                                  |
| scimark_monte_carlo     | 72.3 ms                                                | 46.1 ms: 1.57x faster                                  |
| scimark_sor             | 126 ms                                                 | 78.1 ms: 1.61x faster                                  |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.77 ms: 1.25x faster                                  |
| spectral_norm           | 95.8 ms                                                | 71.7 ms: 1.34x faster                                  |
| sqlglot_parse           | 1.33 ms                                                | 976 us: 1.36x faster                                   |
| sqlglot_transpile       | 1.54 ms                                                | 1.14 ms: 1.35x faster                                  |
| sqlglot_optimize        | 38.1 ms                                                | 30.8 ms: 1.24x faster                                  |
| sqlglot_normalize       | 198 ms                                                 | 167 ms: 1.19x faster                                   |
| sqlite_synth            | 1.50 us                                                | 1.43 us: 1.04x faster                                  |
| sympy_expand            | 275 ms                                                 | 240 ms: 1.14x faster                                   |
| sympy_integrate         | 13.3 ms                                                | 11.3 ms: 1.17x faster                                  |
| sympy_sum               | 93.5 ms                                                | 85.0 ms: 1.10x faster                                  |
| sympy_str               | 169 ms                                                 | 150 ms: 1.13x faster                                   |
| telco                   | 3.63 ms                                                | 3.35 ms: 1.08x faster                                  |
| thrift                  | 577 us                                                 | 433 us: 1.33x faster                                   |
| unpack_sequence         | 38.2 ns                                                | 30.4 ns: 1.26x faster                                  |
| unpickle                | 10.0 us                                                | 9.84 us: 1.02x faster                                  |
| unpickle_list           | 2.66 us                                                | 2.56 us: 1.04x faster                                  |
| unpickle_pure_python    | 204 us                                                 | 151 us: 1.35x faster                                   |
| xml_etree_parse         | 100 ms                                                 | 92.9 ms: 1.08x faster                                  |
| xml_etree_iterparse     | 69.0 ms                                                | 65.5 ms: 1.05x faster                                  |
| xml_etree_generate      | 54.5 ms                                                | 47.0 ms: 1.16x faster                                  |
| xml_etree_process       | 45.1 ms                                                | 34.4 ms: 1.31x faster                                  |
| Geometric mean          | (ref)                                                  | 1.24x faster                                           |
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-python-v3.10.4-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
