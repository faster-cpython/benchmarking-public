
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 30a306c
- commit date: 2023-03-25
- overall geometric mean: 1.19x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 168 ms: 1.20x faster                                   |
| chameleon      | 5.84 ms                                                | 4.51 ms: 1.30x faster                                  |
| docutils       | 1.78 sec                                               | 1.51 sec: 1.18x faster                                 |
| html5lib       | 44.1 ms                                                | 36.7 ms: 1.20x faster                                  |
| tornado_http   | 91.9 ms                                                | 69.1 ms: 1.33x faster                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 60.6 ms: 1.55x faster                                  |
| float          | 72.3 ms                                                | 53.1 ms: 1.36x faster                                  |
| pidigits       | 282 ms                                                 | 280 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 77.0 ms: 1.25x faster                                  |
| regex_v8       | 17.5 ms                                                | 16.1 ms: 1.09x faster                                  |
| regex_dna      | 160 ms                                                 | 152 ms: 1.05x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.71 ms: 1.11x slower                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 194 us: 1.46x faster                                   |
| unpickle_pure_python | 203 us                                                 | 151 us: 1.35x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.24 ms: 1.34x faster                                  |
| xml_etree_process    | 45.1 ms                                                | 37.0 ms: 1.22x faster                                  |
| xml_etree_parse      | 107 ms                                                 | 97.8 ms: 1.10x faster                                  |
| xml_etree_generate   | 54.3 ms                                                | 52.0 ms: 1.04x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.03x faster                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 70.7 ms: 1.03x faster                                  |
| unpickle             | 9.77 us                                                | 9.71 us: 1.01x faster                                  |
| unpickle_list        | 2.66 us                                                | 2.68 us: 1.01x slower                                  |
| pickle               | 7.36 us                                                | 7.45 us: 1.01x slower                                  |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| pickle_list          | 2.83 us                                                | 2.87 us: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.3 ms: 1.02x faster                                  |
| python_startup_no_site | 9.73 ms                                                | 10.3 ms: 1.06x slower                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.40 ms: 1.42x faster                                  |
| genshi_xml      | 37.6 ms                                                | 29.4 ms: 1.28x faster                                  |
| django_template | 27.3 ms                                                | 21.9 ms: 1.25x faster                                  |
| genshi_text     | 18.4 ms                                                | 14.9 ms: 1.23x faster                                  |
| Geometric mean  | (ref)                                                  | 1.29x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-darwin-arm64-python-main-3.12.0a6+-30a306c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.62 ms: 1.97x faster                                  |
| logging_silent          | 119 ns                                                 | 66.6 ns: 1.79x faster                                  |
| richards                | 51.4 ms                                                | 31.5 ms: 1.63x faster                                  |
| nbody                   | 94.1 ms                                                | 60.6 ms: 1.55x faster                                  |
| scimark_lu              | 110 ms                                                 | 71.4 ms: 1.54x faster                                  |
| async_tree_memoization  | 493 ms                                                 | 326 ms: 1.51x faster                                   |
| raytrace                | 328 ms                                                 | 222 ms: 1.48x faster                                   |
| pickle_pure_python      | 284 us                                                 | 194 us: 1.46x faster                                   |
| asyncio_tcp             | 673 ms                                                 | 462 ms: 1.46x faster                                   |
| scimark_sor             | 127 ms                                                 | 88.0 ms: 1.44x faster                                  |
| hexiom                  | 6.32 ms                                                | 4.42 ms: 1.43x faster                                  |
| crypto_pyaes            | 78.0 ms                                                | 54.8 ms: 1.42x faster                                  |
| go                      | 165 ms                                                 | 116 ms: 1.42x faster                                   |
| mako                    | 10.5 ms                                                | 7.40 ms: 1.42x faster                                  |
| chaos                   | 66.8 ms                                                | 47.2 ms: 1.41x faster                                  |
| async_tree_none         | 402 ms                                                 | 290 ms: 1.39x faster                                   |
| scimark_monte_carlo     | 72.2 ms                                                | 52.1 ms: 1.39x faster                                  |
| async_tree_io           | 1.02 sec                                               | 740 ms: 1.38x faster                                   |
| float                   | 72.3 ms                                                | 53.1 ms: 1.36x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 151 us: 1.35x faster                                   |
| pycparser               | 915 ms                                                 | 680 ms: 1.35x faster                                   |
| json_dumps              | 8.38 ms                                                | 6.24 ms: 1.34x faster                                  |
| tornado_http            | 91.9 ms                                                | 69.1 ms: 1.33x faster                                  |
| deepcopy_memo           | 34.5 us                                                | 26.0 us: 1.33x faster                                  |
| pyflate                 | 453 ms                                                 | 343 ms: 1.32x faster                                   |
| spectral_norm           | 96.4 ms                                                | 73.1 ms: 1.32x faster                                  |
| chameleon               | 5.84 ms                                                | 4.51 ms: 1.30x faster                                  |
| genshi_xml              | 37.6 ms                                                | 29.4 ms: 1.28x faster                                  |
| thrift                  | 586 us                                                 | 460 us: 1.28x faster                                   |
| pprint_safe_repr        | 609 ms                                                 | 480 ms: 1.27x faster                                   |
| pprint_pformat          | 1.24 sec                                               | 980 ms: 1.27x faster                                   |
| logging_format          | 5.01 us                                                | 3.99 us: 1.26x faster                                  |
| regex_compile           | 96.6 ms                                                | 77.0 ms: 1.25x faster                                  |
| logging_simple          | 4.63 us                                                | 3.69 us: 1.25x faster                                  |
| django_template         | 27.3 ms                                                | 21.9 ms: 1.25x faster                                  |
| sqlalchemy_imperative   | 9.03 ms                                                | 7.23 ms: 1.25x faster                                  |
| sqlglot_parse           | 1.33 ms                                                | 1.07 ms: 1.24x faster                                  |
| deepcopy                | 278 us                                                 | 224 us: 1.24x faster                                   |
| sqlglot_transpile       | 1.54 ms                                                | 1.25 ms: 1.23x faster                                  |
| create_gc_cycles        | 876 us                                                 | 710 us: 1.23x faster                                   |
| genshi_text             | 18.4 ms                                                | 14.9 ms: 1.23x faster                                  |
| scimark_fft             | 232 ms                                                 | 189 ms: 1.23x faster                                   |
| dulwich_log             | 37.1 ms                                                | 30.2 ms: 1.23x faster                                  |
| async_tree_cpu_io_mixed | 670 ms                                                 | 546 ms: 1.23x faster                                   |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.84 ms: 1.22x faster                                  |
| xml_etree_process       | 45.1 ms                                                | 37.0 ms: 1.22x faster                                  |
| generators              | 32.9 ms                                                | 27.1 ms: 1.21x faster                                  |
| deepcopy_reduce         | 2.38 us                                                | 1.97 us: 1.21x faster                                  |
| 2to3                    | 202 ms                                                 | 168 ms: 1.20x faster                                   |
| html5lib                | 44.1 ms                                                | 36.7 ms: 1.20x faster                                  |
| docutils                | 1.78 sec                                               | 1.51 sec: 1.18x faster                                 |
| sqlglot_optimize        | 38.0 ms                                                | 32.4 ms: 1.17x faster                                  |
| fannkuch                | 317 ms                                                 | 271 ms: 1.17x faster                                   |
| mypy2                   | 308 ms                                                 | 264 ms: 1.17x faster                                   |
| unpack_sequence         | 38.7 ns                                                | 33.3 ns: 1.16x faster                                  |
| sqlalchemy_declarative  | 74.8 ms                                                | 64.6 ms: 1.16x faster                                  |
| bench_thread_pool       | 548 us                                                 | 475 us: 1.16x faster                                   |
| sympy_integrate         | 13.4 ms                                                | 11.8 ms: 1.14x faster                                  |
| sqlglot_normalize       | 197 ms                                                 | 177 ms: 1.11x faster                                   |
| sympy_expand            | 276 ms                                                 | 250 ms: 1.10x faster                                   |
| json                    | 3.10 ms                                                | 2.81 ms: 1.10x faster                                  |
| xml_etree_parse         | 107 ms                                                 | 97.8 ms: 1.10x faster                                  |
| regex_v8                | 17.5 ms                                                | 16.1 ms: 1.09x faster                                  |
| sympy_str               | 169 ms                                                 | 156 ms: 1.08x faster                                   |
| mdp                     | 1.67 sec                                               | 1.54 sec: 1.08x faster                                 |
| sqlite_synth            | 1.47 us                                                | 1.36 us: 1.08x faster                                  |
| coroutines              | 20.2 ms                                                | 18.8 ms: 1.07x faster                                  |
| nqueens                 | 68.1 ms                                                | 63.7 ms: 1.07x faster                                  |
| meteor_contest          | 78.6 ms                                                | 73.8 ms: 1.07x faster                                  |
| sympy_sum               | 94.3 ms                                                | 88.6 ms: 1.06x faster                                  |
| telco                   | 3.68 ms                                                | 3.46 ms: 1.06x faster                                  |
| regex_dna               | 160 ms                                                 | 152 ms: 1.05x faster                                   |
| xml_etree_generate      | 54.3 ms                                                | 52.0 ms: 1.04x faster                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.03x faster                                  |
| xml_etree_iterparse     | 72.6 ms                                                | 70.7 ms: 1.03x faster                                  |
| python_startup          | 12.6 ms                                                | 12.3 ms: 1.02x faster                                  |
| pathlib                 | 28.8 ms                                                | 28.2 ms: 1.02x faster                                  |
| pidigits                | 282 ms                                                 | 280 ms: 1.01x faster                                   |
| unpickle                | 9.77 us                                                | 9.71 us: 1.01x faster                                  |
| unpickle_list           | 2.66 us                                                | 2.68 us: 1.01x slower                                  |
| comprehensions          | 17.7 us                                                | 17.8 us: 1.01x slower                                  |
| pickle                  | 7.36 us                                                | 7.45 us: 1.01x slower                                  |
| pickle_dict             | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| gc_traversal            | 2.40 ms                                                | 2.43 ms: 1.01x slower                                  |
| pickle_list             | 2.83 us                                                | 2.87 us: 1.02x slower                                  |
| python_startup_no_site  | 9.73 ms                                                | 10.3 ms: 1.06x slower                                  |
| regex_effbot            | 2.45 ms                                                | 2.71 ms: 1.11x slower                                  |
| bench_mp_pool           | 41.0 ms                                                | 46.2 ms: 1.13x slower                                  |
| async_generators        | 233 ms                                                 | 267 ms: 1.15x slower                                   |
| dask                    | 258 ms                                                 | 327 ms: 1.27x slower                                   |
| coverage                | 40.8 ms                                                | 60.8 ms: 1.49x slower                                  |
| Geometric mean          | (ref)                                                  | 1.19x faster                                           |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.15x
